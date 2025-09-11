from my_tool.search_tool import tavily_search


def search_tool_for_agent(query: str):
    """
    Wrapper for AI agents to call Tavily search.
    Returns only the answer + sources in a clean format.
    """
    data = tavily_search(query, max_results=3)

    return {
        "answer": data.get("answer"),
        "sources": [
            {
                "title": r.get("title"),
                "url": r.get("url"),
                "snippet": r.get("content") or r.get("raw_content"),
            }
            for r in data.get("results")
        ],
    }
