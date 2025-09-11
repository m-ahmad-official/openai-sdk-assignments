from typing import Any
from agents import (
    output_guardrail,
    RunContextWrapper,
    GuardrailFunctionOutput,
    Runner,
    Agent,
)
from my_agent.politics_agent import politics_agent


@output_guardrail
async def check_output(
    ctx: RunContextWrapper[Any], agent: Agent[Any], output: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(politics_agent, output, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.contains_politics,
    )
