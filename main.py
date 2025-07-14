from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os

# ✅ Load environment variables
load_dotenv()

# ✅ Optional: Confirm GROQ_API_KEY is loaded
print("🔐 GROQ_API_KEY from env:", os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        print(f"✅ Received query: {query.question}")

        graph = GraphBuilder(model_provider="groq")
        print("✅ GraphBuilder initialized.")

        react_app = graph()
        print("✅ Graph built.")

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph_png", "wb") as f:
            f.write(png_graph)   
        print(f"Graph saved as 'my_graph_png' in {os.getcwd()}")
        
        #Assesing request is a pydantic object like: {"question": "yourtext"}
        messages = {"messages": [{"role": "user", "content": query.question}]}
        print(f"✅ Invoking graph with message: {messages}")
        
        output = react_app.invoke(messages)
        print("✅ Output received.")

        # if resutls is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content # Last API response
        else:
            final_output = str(output)
        
        # RETURN a JSON response here
        return JSONResponse(content={"answer": final_output})
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})