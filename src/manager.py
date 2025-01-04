# Manager agent that orchestrates the sub-agents
from smolagents import CodeAgent, ManagedAgent, HfApiModel
from .flight_agent import create_flight_agent
from .hotel_agent import create_hotel_agent
from .weather_agent import create_weather_agent

def create_manager_agent():
    # Build sub-agents
    flight_agent = create_flight_agent()
    hotel_agent = create_hotel_agent()
    weather_agent = create_weather_agent()

    # Wrap them as ManagedAgents
    flight_managed = ManagedAgent(
        agent=flight_agent,
        name="flight_agent",
        description="Agent that can search flights",
        provide_run_summary=False,  # or True if you want
    )
    hotel_managed = ManagedAgent(
        agent=hotel_agent,
        name="hotel_agent",
        description="Agent that finds hotels in a city",
    )
    weather_managed = ManagedAgent(
        agent=weather_agent,
        name="weather_agent",
        description="Agent that checks the temperature and conditions of a city",
    )

    # Create the top-level CodeAgent that orchestrates
    manager_model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")  # example
    manager = CodeAgent(
        tools=[],  # no direct tools, we have sub-agents instead
        model=manager_model,
        managed_agents=[
            flight_managed,
            hotel_managed,
            weather_managed,
        ],
        max_iterations=6,
        additional_authorized_imports=["time"],  # etc.
    )
    return manager