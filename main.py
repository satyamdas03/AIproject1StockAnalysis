from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = StockAnalysisAgents()
    tasks = StockAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.company)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
    filings_task = tasks.filings_analysis(financial_analyst_agent)
    recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        filings_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  company = input(
    dedent("""
      What is the company you want to analyze?
    """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

# This code defines a class FinancialCrew that uses agents and tasks from the CrewAI library to perform a financial analysis of a specified company. 
# Crew: Imported from crewai, used to manage and execute the agents and tasks.
# dedent: Imported from textwrap, used to remove any common leading whitespace from a string.
# StockAnalysisAgents: Custom module that presumably contains definitions for various financial analysis agents.
# StockAnalysisTasks: Custom module that presumably contains definitions for various financial analysis tasks.
# load_dotenv: Loads environment variables from a .env file into the Python environment.
# run: Method that sets up and runs the financial analysis.
# Agents and Tasks:
# Initializes instances of StockAnalysisAgents and StockAnalysisTasks.
# Creates instances of specific agents: research_analyst_agent, financial_analyst_agent, and investment_advisor_agent.
# Creates instances of specific tasks: research_task, financial_task, filings_task, and recommend_task, each assigned to an appropriate agent.
# Crew:
# Creates a Crew instance with the list of agents and tasks.
# Sets verbose=True to enable detailed logging/output.
# Calls the kickoff method of the Crew instance to execute the tasks and collect the results.
# Returns: The result of the crew execution.
# Main Block:
# Prints a welcome message.
# Prompts the user to input the company they want to analyze.
# Creates an instance of FinancialCrew with the specified company.
# Runs the financial analysis by calling the run method.
# Prints the resulting report.
# Summary
# The code sets up a financial analysis pipeline for a specified company using multiple agents and tasks. It defines a FinancialCrew class that:

# Initializes with a company name.
# Sets up and executes various financial analysis tasks using predefined agents.
# Runs the tasks within a Crew instance.
# Collects and prints the results of the analysis.