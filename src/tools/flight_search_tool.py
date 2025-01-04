from smolagents import tool

@tool
def flight_search_tool(origin: str, destination: str, date: str = None) -> str:
    """
    Search flights from `origin` to `destination` on a specific `date`.

    Args:
        origin (str): The departure location (airport code or city).
        destination (str): The arrival location (airport code or city).
        date (str): The travel date in YYYY-MM-DD format. Defaults to None if unspecified.

    Returns:
        str: Mock flight info, e.g. "Mock flight from LAX to JFK..."
    """
    return f"Mock flight from {origin} to {destination} on {date or 'some date'}, Price: $299"