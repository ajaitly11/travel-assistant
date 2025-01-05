import gradio as gr
from .manager import create_manager_agent

manager = create_manager_agent()

def plan_trip(city, origin, date):
    """
    We parse user inputs, do sense checks, then pass instructions to the manager.
    If origin == city, we can do an immediate error or let the manager handle it.
    """
    if not city or not origin or not date:
        return "Error: Missing city/origin/date."

    if city.strip().lower() == origin.strip().lower():
        return "Error: origin and destination are the same!"

    instruction = (
        f"I want to travel from {origin} to {city} on {date}. "
        "Please find me a single-journey flight, some hotel options with their prices, and the historical weather for the city in that month, then combine the results."
    )

    result = manager.run(instruction)
    return str(result)

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Tracy - My Travel Planner Agent")

        city_box = gr.Textbox(label="Destination City", value="")
        origin_box = gr.Textbox(label="Origin City", value="")
        date_box = gr.Textbox(label="Travel Date (YYYY-MM-DD)", value="")

        output_box = gr.Textbox(label="Agent Output")

        submit_btn = gr.Button("Plan Trip!")
        submit_btn.click(
            fn=plan_trip,
            inputs=[city_box, origin_box, date_box],
            outputs=output_box
        )

        demo.launch()

if __name__ == "__main__":
    main()