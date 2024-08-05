import os

import requests

from langchain.tools import tool
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from sec_api import QueryApi
from unstructured.partition.html import partition_html

class SECTools():
  @tool("Search 10-Q form")
  def search_10q(data):
    """
    Useful to search information from the latest 10-Q form for a
    given stock.
    The input to this tool should be a pipe (|) separated text of
    length two, representing the stock ticker you are interested and what
    question you have from it.
		For example, `AAPL|what was last quarter's revenue`.
    """
    stock, ask = data.split("|")
    queryApi = QueryApi(api_key=os.environ['SEC_API_API_KEY'])
    query = {
      "query": {
        "query_string": {
          "query": f"ticker:{stock} AND formType:\"10-Q\""
        }
      },
      "from": "0",
      "size": "1",
      "sort": [{ "filedAt": { "order": "desc" }}]
    }

    fillings = queryApi.get_filings(query)['filings']
    if len(fillings) == 0:
      return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
    link = fillings[0]['linkToFilingDetails']
    answer = SECTools.__embedding_search(link, ask)
    return answer

  @tool("Search 10-K form")
  def search_10k(data):
    """
    Useful to search information from the latest 10-K form for a
    given stock.
    The input to this tool should be a pipe (|) separated text of
    length two, representing the stock ticker you are interested, what
    question you have from it.
    For example, `AAPL|what was last year's revenue`.
    """
    stock, ask = data.split("|")
    queryApi = QueryApi(api_key=os.environ['SEC_API_API_KEY'])
    query = {
      "query": {
        "query_string": {
          "query": f"ticker:{stock} AND formType:\"10-K\""
        }
      },
      "from": "0",
      "size": "1",
      "sort": [{ "filedAt": { "order": "desc" }}]
    }

    fillings = queryApi.get_filings(query)['filings']
    if len(fillings) == 0:
      return "Sorry, I couldn't find any filling for this stock, check if the ticker is correct."
    link = fillings[0]['linkToFilingDetails']
    answer = SECTools.__embedding_search(link, ask)
    return answer

  def __embedding_search(url, ask):
    text = SECTools.__download_form_html(url)
    elements = partition_html(text=text)
    content = "\n".join([str(el) for el in elements])
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 150,
        length_function = len,
        is_separator_regex = False,
    )
    docs = text_splitter.create_documents([content])
    retriever = FAISS.from_documents(
      docs, OpenAIEmbeddings()
    ).as_retriever()
    answers = retriever.get_relevant_documents(ask, top_k=4)
    answers = "\n\n".join([a.page_content for a in answers])
    return answers

  def __download_form_html(url):
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
      'Cache-Control': 'max-age=0',
      'Dnt': '1',
      'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
      'Sec-Ch-Ua-Mobile': '?0',
      'Sec-Ch-Ua-Platform': '"macOS"',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'none',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    return response.text


# This code defines a class called SECTools with tools to search and retrieve specific information from the latest 10-Q and 10-K forms filed by companies with the SEC (Securities and Exchange Commission). @tool("Search 10-Q form"): Registers the search_10q method as a tool named "Search 10-Q form".
# def search_10q(data): Defines a method that takes a pipe-separated string (data) containing the stock ticker and a question.
# Functionality:
# Splits the input into stock and ask.
# Queries the SEC API for the latest 10-Q filing for the given stock.
# If a filing is found, it retrieves the link to the filing details and calls the __embedding_search method to get the answer to the question.
# Returns the answer or an error message if no filing is found.
# @tool("Search 10-K form"): Registers the search_10k method as a tool named "Search 10-K form".
# def search_10k(data): Defines a method that takes a pipe-separated string (data) containing the stock ticker and a question.
# Functionality:
# Splits the input into stock and ask.
# Queries the SEC API for the latest 10-K filing for the given stock.
# If a filing is found, it retrieves the link to the filing details and calls the __embedding_search method to get the answer to the question.
# Returns the answer or an error message if no filing is found.
# Private Method: __embedding_search
#   Downloads and parses the HTML content of the filing from the given URL.
#   Uses the partition_html function to break the content into elements.
#   Joins the elements into a single string.
#   Splits the string into smaller chunks using CharacterTextSplitter.
#   Creates a retriever using FAISS and OpenAIEmbeddings to find the most relevant chunks that answer the question.
#   Returns the concatenated answers.
# Private Method: __download_form_html
#   Downloads the HTML content from the given URL using the specified headers to mimic a web browser request.
# The SECTools class provides tools to search for specific information from the latest 10-Q and 10-K forms filed by companies. It uses the SEC API to retrieve the filings, downloads the HTML content of the filings, and then uses text processing and embedding search techniques to find and return the relevant information based on a user's query.