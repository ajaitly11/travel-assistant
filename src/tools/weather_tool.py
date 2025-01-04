from smolagents import tool

@tool
def weather_tool(city: str) -> str:
    """
    Returns weather data (temperature, conditions) for a city. (Currently a mock/dummy)
    Args:
        city (str): City to check
    """
    # dummy example for now
    return "72F, Partly Cloudy"