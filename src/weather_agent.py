from smolagents import ToolCallingAgent, HfApiModel
from .tools.weather_tool import weather_tool

def create_weather_agent():
    tools = [weather_tool]
    model = HfApiModel("meta-llama/Llama-3.3-70B-Instruct")

    weather_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=3,
    )
    return weather_agent