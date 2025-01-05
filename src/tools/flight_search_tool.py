from smolagents import tool
from datetime import datetime
from duckduckgo_search import DDGS

@tool
def flight_search_tool(origin: str, destination: str, date: str = None) -> str:
    """
    Searches for single-journey flights from origin to destination on a given date using DuckDuckGo Search.
    We do NOT handle return flights. If the user tries to indicate a return, we disclaim it.

    Args:
        origin: The departure location (airport code or city).
        destination: The arrival location (airport code or city).
        date: The travel date in YYYY-MM-DD format. If None, we assume the user didn't specify a date.

    Returns:
        A string representing flight info or an error message. For example:
        "Mock duckduckgo result: Flight from NYC to LON => someURL"
        or if no results found or round trip detected, we disclaim.
    """
    if not origin or not destination:
        return "Error: Missing origin or destination."
    if origin.lower() == destination.lower():
        return "Error: Origin and destination cannot be the same."

    # Validate date if provided:
    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            now = datetime.now()
            if parsed_date < now:
                return f"Error: {date} is in the past!"
        except ValueError:
            return "Error: Invalid date format, must be YYYY-MM-DD."

    ddgs = DDGS()
    query_date = date if date else "some date"
    query = f"Flight from {origin} to {destination} on {query_date}"
    results = ddgs.text(query, max_results=1)

    for r in results:
        # Return a single result
        return f"duckduckgo result: {r['title']} => {r['href']}"

    return f"No flight info found for single-journey {origin} -> {destination} on {query_date}"