from my_agent.search_agent import search_tool_for_agent


query = input("Enter your question: ")
result = search_tool_for_agent(query)

print("\n", result["answer"], "\n")
print("Sources:")
for s in result["sources"]:
    print(f"- {s['title']} ({s['url']})")
    print(f"  {s['snippet']}....\n")
