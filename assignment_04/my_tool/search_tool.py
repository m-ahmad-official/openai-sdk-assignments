import requests
from my_config.tavily_config import api_key, base_url


def tavily_search(query: str, max_results: int = 5):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    json = {
        "query": query,
        "max_results": max_results,
        "include_answer": True,
        "include_raw_content": True,
    }

    response = requests.post(base_url, json=json, headers=headers)

    return response.json()
