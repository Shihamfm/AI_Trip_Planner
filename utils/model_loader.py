
import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class Configloader:
    
    
    def __init__(self):
        print(f"Loading config....")
        self.config = load_config()
        
    def __getitem__(self, key):
        return self.config[key]
    
    
class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config: Optional[Configloader] = Field(default=None, exclude=None)
    
    def model_past_init(self, __context: Any) -> None:
        self.config = Configloader()
        
    class Config:
        arbitary_types_allowed = True
        
    def load_llm(self):
        """Load and return the LLM model.
        """

        if self.model_provider == "groq":
            print("Loading LLM from Groq.......")
            print(f"Loading model from provider: {self.model_provider}")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        
        elif self.model_provider == "openai":
            print("Loading LLM from OPenAI.......")
            print(f"Loading model from provider: {self.model_provider}")
            openai_api_key = os.getenv("OPEN_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model=model_name, api_key=openai_api_key)
            
        return llm
