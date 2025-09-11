from agents import Agent
from guardrail_function.input_guardrail_function import check_input
from guardrail_function.output_guardrail_function import check_output
from my_config.gemini_config import gemini_model

agent = Agent(
    "CustomerSupportAgent",
    instructions="You are a customer support agent. You help customers with their questions.",
    model=gemini_model,
    input_guardrails=[check_input],
    output_guardrails=[check_output],
)
