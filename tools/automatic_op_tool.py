import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper


@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers

    Args:
        a (int): the first integer
        b (int): the second integer

    Returns:
        int: the product of a and b
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """
    Add two integers

    Args:
        a (int): the first integer
        b (int): the second integer

    Returns:
        int: the sum of a and b
    """
    return a + b

@tool
def currency_converter(from_curr:str, to_curr:str, value:float) -> float:
    """
    Convert currency from one type to another using Alpha Vantage API.

    Args:
        from_curr (str): The currency to convert from.
        to_curr (str): The currency to convert to.
        amount (float): The amount of money to convert.

    Returns:
        float: The converted amount in the target currency.
    """
    os.environ["ALPHA_VANTAGE_API_KEY"] = os.getenv("ALPHA_VANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage.convert_currency(from_curr, to_curr)
    exhange_rate = response.get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate")
    return value * float(exhange_rate)