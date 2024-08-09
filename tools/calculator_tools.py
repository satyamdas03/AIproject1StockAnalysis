# to perform the necessary calculations
from langchain.tools import tool


class CalculatorTools():

  @tool("Make a calculation")
  def calculate(operation):
    """Useful to perform any mathematical calculations, 
    like sum, minus, multiplication, division, etc.
    The input to this tool should be a mathematical 
    expression, a couple examples are `200*7` or `5000/2*10`
    """
    return eval(operation)
  

# @tool("Make a calculation"): This is a decorator that registers the calculate method as a tool within the LangChain framework, giving it the name "Make a calculation".
# def calculate(operation):: Defines a method named calculate that takes one parameter, operation.
# The docstring ("""...""") provides a description of what the method does and examples of valid inputs.
# return eval(operation): This line evaluates the mathematical expression passed as the operation parameter and returns the result. The eval function in Python takes a string and evaluates it as a Python expression.
# Example Usage
# If you call calculate("200*7"), the method will evaluate the expression and return 1400. Similarly, calling calculate("5000/2*10") will return 25000.

# Summary
# This code provides a simple calculator tool that can evaluate and return the result of mathematical expressions. The use of the eval function allows for flexibility in the types of operations that can be performed, including addition, subtraction, multiplication, and division.

# Note: While eval is powerful, it can be dangerous if used with untrusted input, as it can execute arbitrary code. In a production environment, you should ensure that the input to eval is safe or consider using a safer alternative.