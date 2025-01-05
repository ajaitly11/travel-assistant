# This is a simple tool that searches for hotels in a given city using DuckDuckGo Search.
from smolagents import tool
from duckduckgo_search import DDGS

@tool
def hotel_search_tool(city: str) -> str:
    """
    Finds hotel info in a given city using DuckDuckGo Search.

    Args:
        city: The city to search for hotels.

    Returns:
        A string with top hotel search result or an error message.
    """
    if not city:
        return "Error: City is required."
    
    ddgs = DDGS()
    query = f"Hotels in {city} near city center"
    results = ddgs.text(query, max_results=1)
    for r in results:
        return f"Hotels found (mock): {r['title']} => {r['href']}"
    
    return f"No hotel info found for {city}"