from dotenv import load_dotenv
load_dotenv()

# now import your modules that depend on the env variables
from agent.agentic_workflow import GraphBuilder

if __name__ == "__main__":
    # Build the graph
    graph = GraphBuilder()()
    
    # Provide a test input
    input_data = {
        "messages": [{"role": "user", "content": "What is the capital of France?"}]
    }

    print("🚀 Invoking graph with test message...")
    result = graph.invoke(input_data)

    if isinstance(result, dict) and "messages" in result:
        print("AI Response:", result["messages"][-1].content)
    else:
        print("Raw Result:", result)
