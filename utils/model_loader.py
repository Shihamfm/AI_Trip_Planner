import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# ✅ Define ConfigLoader class first
class ConfigLoader:
    def __init__(self):
        print("🔄 Loading config...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

# ✅ Then use it in ModelLoader
class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """Load and return the LLM model."""
        if self.config is None:
            self.config = ConfigLoader()

        if self.model_provider == "groq":
            print("🔧 Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            return ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("🔧 Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            return ChatOpenAI(model=model_name, api_key=openai_api_key)
