import os
from dotenv import load_dotenv
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

# Load environment variables from .env file
load_dotenv()

# Add your API key here, if necessary
# api_key = os.getenv("YOUR_API_KEY")

class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role='The Best Financial Analyst',
            goal="""Impress all customers with your financial data 
            and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
            lots of expertise in stock market analysis and investment
            strategies that is working for a super important customer.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )

    def research_analyst(self):
        return Agent(
            role='Staff Research Analyst',
            goal="""Being the best at gather, interpret data and amaze
            your customer with it""",
            backstory="""Known as the BEST research analyst, you're
            skilled in sifting through news, company announcements, 
            and market sentiments. Now you're working on a super 
            important customer""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )

    def investment_advisor(self):
        return Agent(
            role='Private Investment Advisor',
            goal="""Impress your customers with full analyses over stocks
            and complete investment recommendations""",
            backstory="""You're the most experienced investment advisor
            and you combine various analytical insights to formulate
            strategic investment advice. You are now working for
            a super important customer you need to impress.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool()
            ]
        )

# Example usage
if __name__ == "__main__":
    agents = StockAnalysisAgents()
    financial_analyst_agent = agents.financial_analyst()
    research_analyst_agent = agents.research_analyst()
    investment_advisor_agent = agents.investment_advisor()

    # Now you can use the agents as needed
    # Example: print details of the financial analyst agent
    print(financial_analyst_agent)

# The code sets up a system for generating different types of agents specialized in financial analysis, research, and investment advising. Each agent is equipped with a set of tools to perform tasks related to their role. The environment variables are loaded from a .env file, allowing for secure configuration of API keys and other sensitive information.