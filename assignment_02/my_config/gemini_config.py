from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

api_key = config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")

gemini_client = AsyncOpenAI(api_key=api_key, base_url=base_url)
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=gemini_client
)
