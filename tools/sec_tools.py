# sec_tools 
import os
import requests
from langchain.tools import tool
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

