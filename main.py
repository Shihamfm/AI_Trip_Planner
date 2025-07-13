from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
        
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph_png", "wb") as f:
            f.write(png_graph)
            
        print(f"Graph saved as 'my_graph_png' in {os.getcwd()}")
        
        #Assesing request is a pydantic object like: {"question": "yourtext"}
        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)
        
        # if resutls is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content # Last API response
        else:
            final_output = str(output)
            
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})