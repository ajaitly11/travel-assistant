from smolagents import ToolCallingAgent, HfApiModel
from .tools.flight_search_tool import flight_search_tool

def create_flight_agent():
    tools = [flight_search_tool]

    # Can modify to any other model
    model = HfApiModel(
        model_id="codellama/CodeLlama-34b-Instruct-hf", 
        token=None  # or your HF token if needed
    )

    flight_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=3
    )
    return flight_agent