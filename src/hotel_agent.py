from smolagents import ToolCallingAgent, HfApiModel
from .tools.hotel_search_tool import hotel_search_tool

def create_hotel_agent():
    tools = [hotel_search_tool]
    model = HfApiModel("meta-llama/Llama-3.3-70B-Instruct")

    hotel_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=3,
    )
    return hotel_agent