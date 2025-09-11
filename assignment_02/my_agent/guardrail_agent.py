from agents import Agent
from my_config.gemini_config import gemini_model
from data_schema.my_data_schema import MyDataType

guardrail_agent = Agent(
    name="Guradrial Agent for Hotel",
    instructions="Check queries for hotel",
    model=gemini_model,
    output_type=MyDataType,
)
