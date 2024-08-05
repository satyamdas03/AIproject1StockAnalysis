# to browse the internet
import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing research and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do research about a given topic.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)
  
# This code defines a class BrowserTools with a method scrape_and_summarize_website that is used to scrape and summarize the content of a given website. Here's a step-by-step explanation of what this code does:

# Imports
# json, os, requests: Standard Python libraries for JSON manipulation, environment variable handling, and making HTTP requests.
# Agent, Task from crewai: Classes for creating agents and tasks in the CrewAI framework.
# tool from langchain.tools: A decorator to define a tool.
# partition_html from unstructured.partition.html: A function to partition HTML content into elements.
# Class Definition: BrowserTools
# @tool("Scrape website content"): This decorator registers the scrape_and_summarize_website method as a tool with the name "Scrape website content".
# Method: scrape_and_summarize_website
# Parameters:

# website: The URL of the website to scrape.
# Process:

# Construct API URL: The method constructs the URL for the Browserless API, which is a headless browser service used for scraping website content. It uses an API key stored in the environment variable BROWSERLESS_API_KEY.
# Prepare Payload: A JSON payload is prepared with the URL of the website to be scraped.
# Set Headers: HTTP headers are set to specify the content type and cache control.
# Send Request: An HTTP POST request is sent to the Browserless API with the prepared payload and headers.
# Partition HTML: The response text (HTML content of the website) is partitioned into elements using the partition_html function.
# Combine Content: The partitioned content is joined into a single string, which is then split into chunks of 8000 characters.
# Summarize Content:

# For each chunk of content:
# Create Agent: An Agent is created with the role of "Principal Researcher" and a specific goal and backstory.
# Create Task: A Task is created for the agent, with a description instructing the agent to analyze and summarize the given chunk of content.
# Execute Task: The task is executed, and the summary is appended to the summaries list.
# Combine Summaries: All the summaries are joined into a single string.
# Return Summary: The combined summary of the website content is returned as the output of the method.

# Summary
# The scrape_and_summarize_website method in the BrowserTools class performs the following actions:

# Scrapes the content of a given website using the Browserless API.
# Partitions the HTML content into manageable chunks.
# Uses an AI agent to summarize each chunk.
# Combines the summaries into a final summary of the website content.
# This method is useful for quickly obtaining a summarized version of the content from any given website.