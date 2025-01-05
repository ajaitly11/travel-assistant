from smolagents import ToolCallingAgent, HfApiModel
from .tools.hotel_search_tool import hotel_search_tool

def create_hotel_agent():
    tools = [hotel_search_tool]
    model = HfApiModel(
        model_id="codellama/CodeLlama-34b-Instruct-hf",
    )

    hotel_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=3
    )
    return hotel_agent