from agents import (
    Runner,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    set_tracing_disabled,
)
from my_agent.agent import agent
import asyncio

set_tracing_disabled(True)


async def main():
    try:
        msg = input("Enter your question: ")
        result = await Runner.run(agent, msg)
        print(f"\n\nFinal output : {result.final_output}")

    except InputGuardrailTripwireTriggered:
        print("Input guardrail tripped: invalid prompt (math detected)")

    except OutputGuardrailTripwireTriggered:
        print("Output guardrail tripped: response contained politics")


asyncio.run(main())
