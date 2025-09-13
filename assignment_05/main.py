from agents import Runner, set_tracing_disabled
from agents.exceptions import (
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
)
from my_agent.agents import agents

set_tracing_disabled(True)

try:
    result = Runner.run_sync(
        starting_agent=agents,
        input=input("Enter your query: "),
    )
    print("✅ Final Answer:", result.final_output)


except InputGuardrailTripwireTriggered:
    print("❌ Reject query")


except OutputGuardrailTripwireTriggered:
    print("❌ Blocked Output")
