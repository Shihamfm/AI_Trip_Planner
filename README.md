# ✈️ AI Trip Planner

Welcome to **AI Trip Planner**, an intelligent agentic application that helps you plan your travel trips interactively using cutting-edge AI and multiple APIs!

---

## 🚀 Project Overview

AI Trip Planner is a smart travel assistant designed to help users plan trips by querying various travel-related information:

- Attractions, restaurants, activities, transportation info for any destination
- Real-time weather updates
- Currency conversion for travel budgeting
- Expense calculations

This project leverages **Large Language Models (LLMs)** combined with custom-built tools to provide accurate, context-aware travel plans.

---

## 🔍 Features

- **Conversational AI agent**: Ask travel-related questions naturally.
- **Multiple data sources**: Google Places API, Tavily Search API (fallback), weather APIs, currency converters.
- **Graph-based agent workflow**: Modular architecture to handle multi-step queries.
- **Interactive frontend**: Streamlit app for easy user interaction.
- **Backend API**: FastAPI server hosting the AI logic and tools.
- **Visualized agent workflows** with Mermaid diagrams.

---

## 🛠️ Tech Stack

| Component                 | Technology / Library           |
|---------------------------|-------------------------------|
| AI Models & Tools         | Groq LLM, Langchain, Tavily    |
| Backend API               | FastAPI                        |
| Frontend UI              | Streamlit                     |
| API Integrations          | Google Places, Tavily, Exchange Rate API, Weather API |
| Environment Management    | Python, dotenv                 |
| Agent Workflow            | LangGraph                     |

---

## 📂 Repository Structure


---

## 🔧 Setup & Installation

### 1. Clone the repo

git clone https://github.com/Shihamfm/AI_Trip_Planner.git
cd AI_Trip_Planner

### 2. Create and activate Python environment
python -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file in the root directory with your API keys:

GROQ_API_KEY=your_groq_api_key_here
GPLACES_API_KEY=your_google_places_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here
WEATHER_API_KEY=your_weather_api_key_here

## 🚀 Running the Application

### Start the FastAPI backend server:
streamlit run streamlit_app.py

### Start the Streamlit frontend app:
streamlit run streamlit_app.py

Now open your browser and visit:
http://localhost:8501

## 📝 Usage
Enter your travel query in the chat box (e.g., "Plan a trip to Paris for 5 days").

The AI agent will process your request using the integrated APIs and respond with a detailed travel plan.

Explore attractions, restaurants, weather, currency conversions, and more.

View internal agent workflow graphs saved as my_graph_png for debugging.

## 🛠️ How It Works
User Query is sent from the frontend to the FastAPI backend.

Backend invokes the GraphBuilder which loads the LLM and tools.

The LLM-based agent uses a state graph to call appropriate tools (e.g., place search, weather).

Responses are aggregated and returned as a coherent answer.

Frontend displays the AI-generated travel plan to the user.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or pull requests for new features, bug fixes, or improvements.

## 💬 Contact
Created by Shiham Farook. https://www.linkedin.com/in/shihamfm/
Feel free to reach out for collaboration or questions!