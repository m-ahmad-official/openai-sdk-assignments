from agents import Agent
from my_config.gemini_config import gemini_model
from guardrail_function.input_guardrail_function import input_guardrail_function

hotels_data = {
    "Hotel Sannata": {
        "total_rooms": 200,
        "reserved_rooms": 20,
        "owner": "Mr. Ratan Lal",
    },
    "Hotel Paradise": {
        "total_rooms": 150,
        "reserved_rooms": 10,
        "owner": "Mrs. Sofia Khan",
    },
    "Hotel Ocean View": {
        "total_rooms": 300,
        "reserved_rooms": 30,
        "owner": "Mr. Imran Ali",
    },
}


def generate_instructions(hotels):
    hotel_info_list = []
    for name, details in hotels.items():
        available_rooms = details["total_rooms"] - details["reserved_rooms"]
        hotel_info_list.append(
            f"""
            - Hotel name: {name}
            - Owner: {details['owner']}
            - Total rooms: {details['total_rooms']}
            - Reserved rooms: {details['reserved_rooms']}
            - Available rooms: {available_rooms}
            """
        )
    return f"""
    You are a helpful hotel customer care assistant.
    You can provide information about multiple hotels.
    Here are the hotel details you know:
    {''.join(hotel_info_list)}

    Always answer queries by identifying the correct hotel
    based on the user's question.
    """


hotel_assistant = Agent(
    name="Hotel Customer Care",
    instructions=generate_instructions(hotels_data),
    model=gemini_model,
    input_guardrails=[input_guardrail_function],
)
