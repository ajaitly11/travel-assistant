from smolagents import ToolCallingAgent, HfApiModel
from .tools.flight_search_tool import flight_search_tool
from .tools.hotel_search_tool import hotel_search_tool
from .tools.weather_tool import weather_tool

SYSTEM_PROMPT = """
You are an expert manager agent. The user wants to plan a trip. You can call these tools:
- flight_search_tool(origin=..., destination=..., date=...)
- hotel_search_tool(city=...)
- weather_tool(city=..., date=...) 
- final_answer(...)

**ALWAYS** output your tool calls in valid JSON format. 
**NEVER** pass anything else to the functions except the arguments given above. STRICTLY FOLLOW THIS GUIDELINE
**NEVER** produce random code or partial fences. 
**Stop** after calling final_answer.

You do not have any knowledge of flight details, hotel info, or weather. The only way you can get that info is by calling the correct tool.
No answer from memory is allowed. You do not have real knowledge. You must call the tools for each subtask. If you produce any unrequested text or final answer that uses your memory, that is a violation.

When the user says something like "I want to travel from X to Y on Z," do:
  1. flight_search_tool
  2. hotel_search_tool
  3. weather_tool
Then finalize with final_answer.

If the user’s origin == destination, we can just do final_answer("Error: origin=destination").

Return the combined info in the final_answer text.

Here’s the JSON format for tool calls:

Action:
{
  "tool_name": "...",
  "tool_arguments": { ... }
}

If no more steps are needed, do final_answer(...). 
Stop. Do not show any code blocks or random text.

Now begin.

{{managed_agents_descriptions}}
"""

def create_manager_agent():
    # We define the tools that the manager can call:
    tools = [flight_search_tool, hotel_search_tool, weather_tool]

    # Pick a model for the agent. This is a model that can call the tools.
    model = HfApiModel(
        model_id="codellama/CodeLlama-34b-Instruct-hf",
        token=None,  # Optional, only needed for private models
        timeout=45
    )

    manager_agent = ToolCallingAgent(
        tools=tools,
        model=model,
        max_iterations=5,  
        system_prompt=SYSTEM_PROMPT
    )
    return manager_agent