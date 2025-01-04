from smolagents import tool

@tool
def flight_search_tool(origin: str, destination: str, date: str = None) -> str:
    """
    Searches for flights from the origin to the destination on a specific date.

    Args:
        origin (str): The starting location (for example, airport code or city).
        destination (str): The destination location (for example, airport code or city).
        date (str, optional): Travel date in YYYY-MM-DD format. Defaults to None.

    Returns:
        str: Mock flight details such as price and date info.
    """
    return f"Mock flight from {origin} to {destination} on {date or 'some date'}, Price: $299"