from agents import Agent
from guardrail_function.input_guardrail_function import check_input
from guardrail_function.output_guardrail_function import check_output
from my_config.gemini_config import gemini_model

weather_agent = Agent(
    name="Weather Agent",
    instructions="Provides weather updates.",
    input_guardrails=[check_input],
    output_guardrails=[check_output],
    model=gemini_model,
)


flight_agent = Agent(
    name="Flight Agent",
    instructions="Provides flight schedules and fares.",
    input_guardrails=[check_input],
    output_guardrails=[check_output],
    model=gemini_model,
)

hotel_agent = Agent(
    name="Hotel Agent",
    instructions="Provides hotel availability and bookings.",
    input_guardrails=[check_input],
    output_guardrails=[check_output],
    model=gemini_model,
)

agents = Agent(
    name="Multi agent",
    input_guardrails=[check_input],
    output_guardrails=[check_output],
    model=gemini_model,
    handoffs=[weather_agent, flight_agent, hotel_agent],
)
