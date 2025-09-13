from agents import (
    GuardrailFunctionOutput,
    RunContextWrapper,
    Agent,
    TResponseInputItem,
    output_guardrail,
    Runner,
)
from data_schema.usa_cities_output import UsaCitiesOutPut
from my_config.gemini_config import gemini_model


@output_guardrail
async def check_output(
    ctx: RunContextWrapper,
    agent: Agent,
    output_data: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    output_agent = Agent(
        "OutputGuardrailAgent",
        instructions=("Check and verify if input is related to usa cities."),
        model=gemini_model,
        output_type=UsaCitiesOutPut,
    )

    result = await Runner.run(output_agent, output_data, context=ctx.context)
    final_output: UsaCitiesOutPut = result.final_output

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.is_usa_cities,
    )
