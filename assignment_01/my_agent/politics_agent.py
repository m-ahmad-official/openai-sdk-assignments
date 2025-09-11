from agents import Agent
from data_schema.politics_output import PoliticsOutput
from my_config.gemini_config import gemini_model

politics_agent = Agent(
    "PoliticsGuardrailAgent",
    instructions=(
        "Analyze the response text. Determine if it contains political topics, "
        "political opinions, or references to political figures. "
        "Return contains_politics=True if yes, otherwise False."
    ),
    model=gemini_model,
    output_type=PoliticsOutput,
)
