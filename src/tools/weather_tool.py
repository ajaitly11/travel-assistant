from smolagents import tool
import os
from datetime import datetime
from duckduckgo_search import DDGS

@tool
def weather_tool(city: str, date: str = None) -> str:
    """
    Returns historical weather for a city in the month of the user's travel date.
    This uses DuckDuckGo Search to find typical/historical climate data.

    Args:
        city: The city to check.
        date: Desired date in YYYY-MM-DD format (optional). If not provided, we treat it as 'some date'.

    Returns:
        A string with some "historical weather" snippet from DuckDuckGo, or an error/fallback message.
    """
    if not city:
        return "Error: No city provided."

    # If date is None, just do a search for "some date"
    if not date:
        return _duckduckgo_weather_search(city, month="some")

    # parse date
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Must be YYYY-MM-DD."

    # get month name
    # e.g. dt.strftime("%B") => "March"
    month_name = dt.strftime("%B")

    # do a duckduckgo-based search
    return _duckduckgo_weather_search(city, month=month_name)


def _duckduckgo_weather_search(city: str, month: str) -> str:
    """
    Helper that uses duckduckgo to find "historical weather in {city} during {month}" snippet.
    """
    ddgs = DDGS()
    query = f"historical weather in {city} during {month}"
    results = ddgs.text(query, max_results=1)
    for r in results:
        # return the top snippet
        return f"Historical weather snippet for {city}, {month}: {r['title']} => {r['href']}"
    return f"No results found for historical weather in {city} during {month}"