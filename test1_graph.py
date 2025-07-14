import os
from dotenv import load_dotenv

load_dotenv()  # make sure this is called

print("Loaded GROQ key:", os.getenv("GROQ_API_KEY"))


groq_api_key = os.getenv("GROQ_API_KEY")
print("Loaded GROQ key:", groq_api_key)

from utils.config_loader import load_config

class Configloader:
    def __init__(self):
        print("🔄 Loading config...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class ModelLoader:
    def __init__(self, model_provider="groq"):
        self.model_provider = model_provider
        self.config = Configloader()  # ✅ this sets self.config correctly

    def load_llm(self):
        if self.model_provider == "groq":
            print("🔧 Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("❌ GROQ_API_KEY not found. Check your .env file.")
            model_name = self.config["llm"]["groq"]["model_name"]
            return ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("🔧 Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPEN_API_KEY")
            if not openai_api_key:
                raise ValueError("❌ OPEN_API_KEY not found. Check your .env file.")
            model_name = self.config["llm"]["openai"]["model_name"]
            return ChatOpenAI(model=model_name, api_key=openai_api_key)
