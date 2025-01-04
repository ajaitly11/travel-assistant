from smolagents import ToolCallingAgent, HfApiModel
from .tools.flight_search_tool import flight_search_tool

def create_flight_agent():
    # We can wrap the tool in a list
    tools = [flight_search_tool]
    model = HfApiModel("meta-llama/Llama-3.3-70B-Instruct")  # or any other

    flight_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=3,
        # system_prompt=... (optional custom system prompt),
    )
    return flight_agent