from smolagents import tool

@tool
def flight_search_tool(origin: str, destination: str, date: str = None) -> str:
    """
    Example tool to search flights. (Currently a mock/dummy)
    Args:
        origin (str): The city or airport code you are flying from
        destination (str): The city or airport code you want to go to
        date (str, optional): Travel date in YYYY-MM-DD format
    Returns:
        (str): A string with flight options / best flight found
    """
    # Dummy String for now
    return f"Mock flight from {origin} to {destination} on {date or 'some date'}, Price: $299"