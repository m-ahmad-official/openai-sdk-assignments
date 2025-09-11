from typing import Any
from agents import (
    input_guardrail,
    RunContextWrapper,
    GuardrailFunctionOutput,
    Runner,
    Agent,
    TResponseInputItem,
)

from data_schema.math_output import MathOutPut
from my_config.gemini_config import gemini_model


@input_guardrail
async def check_input(
    ctx: RunContextWrapper[Any],
    agent: Agent[Any],
    input_data: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    input_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if input is related to math",
        model=gemini_model,
        output_type=MathOutPut,
    )
    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.is_math,
    )
