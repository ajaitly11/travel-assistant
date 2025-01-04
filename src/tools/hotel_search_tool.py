from smolagents import tool

@tool
def hotel_search_tool(city: str) -> str:
    """
    Finds hotel info in a given city. (Currently a dummy)
    Args:
        city (str): The city to search for hotels
    Returns:
        (str): hotel listings with prices
    """
    # Dummy response for now
    return f"Mock hotels in {city}: [Hotel A - $150/night, Hotel B - $200/night]"