# Tracy - Multi-Agent Travel Assistant

Welcome to Tracy! This repository demonstrates how to build a simple multi-agent travel planner using the smolagents library from Hugging Face. The smolagents library makes it incredibly easy to create AI “agents” that can call various tools to get specific information, instead of relying on the model’s internal (and often out-of-date) knowledge.

What is this repository?

This repository implements a single manager agent that helps users plan a trip by:
	1.	Searching for a flight (single journey).
	2.	Finding some hotels and their costs.
	3.	Checking weather (historical or forecast) for the chosen date.

All the code demonstrates a ToolCallingAgent approach from smolagents, forcing the AI model to produce valid JSON calls to your tools instead of memorizing or hallucinating. This leads to more robust, controllable outputs.

Key files
	•	main.py
A minimal Gradio UI that prompts for the origin city, destination city, and date, then calls the manager agent.

python -m src.main

to launch the Gradio interface locally.

	•	manager.py
Contains the ToolCallingAgent called manager_agent. It is configured with:
	•	A system prompt (SYSTEM_PROMPT) that instructs the LLM to call:
	•	flight_search_tool (for flight info),
	•	hotel_search_tool (for hotel info),
	•	weather_tool (for historical weather),
	•	then finalize the output via final_answer(...).
	•	The HfApiModel specifying the chosen model, e.g. "codellama/CodeLlama-34b-Instruct-hf".
	•	weather_agent.py, hotel_agent.py, flight_agent.py
Originally, these could define separate agents. In this simplified manager.py, we just pass the tools directly to the manager. However, you can build specialized sub-agents if you want more complex logic.
	•	tools/flight_search_tool.py, tools/hotel_search_tool.py, tools/weather_tool.py
Actual Python “tool” definitions decorated with @tool from smolagents, each one performing a DuckDuckGo search or a mock search to simulate real data.

How does smolagents help?

smolagents provides:
	1.	Simplicity: Instead of manually parsing an LLM’s output for tool calls, you can rely on the ToolCallingAgent or CodeAgent classes to orchestrate multi-step usage of your tools.
	2.	Tool-first approach: All real data must come from tools. The LLM is forced (via system prompts and code) to call these tools instead of hallucinating final answers.
	3.	Support for many models: You can pick different Hugging Face models (e.g. Code Llama, Llama 2, Falcon, GPT) as long as they accept standard chat completions.
	4.	Better control: By requiring valid JSON tool calls, you can detect if the LLM tries to skip the process or memorize data. This yields more consistent, debuggable behavior.

In short, smolagents helps you keep your codebase smaller and your LLM usage more direct and secure, so you spend less time building prompt parsing or chain logic, and more time shipping a reliable multi-agent app.

Installation & Usage
	1.	Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows


	2.	Install dependencies:
'''
pip install -r requirements.txt
'''

	3.	Run:
'''
python -m src.main
'''
	•	This launches a local Gradio UI at http://127.0.0.1:7860.
	•	Enter your origin city, destination city, and travel date, then click Plan Trip!.

	4.	Agentic flow:
	•	The manager agent ToolCallingAgent sees your instructions.
	•	It calls flight_search_tool, hotel_search_tool, weather_tool in JSON, combining their results into one final answer.
	•	The final text is displayed in the Gradio interface.

Customizing
	•	Change the model: In manager.py, swap out "codellama/CodeLlama-34b-Instruct-hf" for another open or private model. Some models might follow instructions better.
	•	Enhance the system prompt: If your LLM tries to skip tool usage, strengthen the system prompt with additional constraints or pick a more instruction-following model.
	•	Add or remove tools: If you want extra data (like local events, currency exchange, etc.), write more @tool methods in tools/, then add them to manager.py.

Disclaimers
	•	The flight/hotel/weather results are often mock or basic DuckDuckGo searches. This is not a production system.
	•	LLMs can sometimes ignore instructions; we rely on structured prompting to minimize hallucinations but it’s still possible.
	•	If you see final answers that are not from the tool calls, you can tweak the prompt or try different models.

Contributing & License

This is a personal/demonstration project. Feel free to fork or submit PRs for improvements. The underlying smolagents library is Apache-2.0 licensed, so this code is also under compatible open-source licensing.

Happy traveling with smolagents and multi-agent AI!