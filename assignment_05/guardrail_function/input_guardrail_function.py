from agents import (
    GuardrailFunctionOutput,
    RunContextWrapper,
    Agent,
    TResponseInputItem,
    input_guardrail,
    Runner,
)
from data_schema.india_cities_output import IndiaCitiesOutPut
from my_config.gemini_config import gemini_model


@input_guardrail
async def check_input(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input_data: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    input_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if input is related to india cities.",
        model=gemini_model,
        output_type=IndiaCitiesOutPut,
    )

    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.is_india_cities,
    )
