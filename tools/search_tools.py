# to search for the best possible outcomes
import json
import os

import requests
from langchain.tools import tool


class SearchTools():
  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet 
    about a a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)

  @tool("Search news on the internet")
  def search_news(query):
    """Useful to search news about a company, stock or any other
    topic and return relevant results"""""
    top_result_to_return = 4
    url = "https://google.serper.dev/news"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['news']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)
  

# son: For working with JSON data.
# os: For accessing environment variables.
# requests: For making HTTP requests.
# tool: A decorator from the langchain.tools module used to define tools within the LangChain framework.
# @tool("Search the internet"): Registers the search_internet method as a tool named "Search the internet".
# def search_internet(query): Defines a method that takes a search query as input.
# Functionality:
# Sets the number of top results to return (top_result_to_return = 4).
# Prepares the API request to the Serper (Google search) API with the given query.
# Sends the request and gets the response.
# Parses the response to extract the top search results.
# Formats the results (title, link, snippet) into a string.
# Returns the formatted string containing the top search results.
# @tool("Search news on the internet"): Registers the search_news method as a tool named "Search news on the internet".
# The SearchTools class provides two tools for searching the internet. The search_internet method performs a general web search, and the search_news method performs a news search. Both methods use the Serper API to fetch results and return the top 4 relevant results formatted as strings.