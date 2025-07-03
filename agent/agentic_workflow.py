
from utils.model_loader import ModelLoader
from prompt_library import SYSTEM_PROMPT
from langgraph import StateGraph, MessageState, END, START
from langgraph import ToolNode, tools_condition

#from tools.weather_info_tool import WeatherInfoTool
#from tools.place_search_tool import PlaceSearchTool
#from tools.expense_calculator_tool import Calculatortool
#from tools.currency_conversion_tool import CurrencyConverterTool



class GraphicBuilder():
    
    
    def __init__(self):
        self.tools = [
            # WeatherInfoTool(),
            # PlaceSearchTool(),    
            # Calculatortool(),
            # CurrencyConverterTool()
        ]
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self, state: MessageState):
        """Main agent function
        """
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messges:", [response]}
    
    def build_graph(self):
        graph_builder = StateGraph(MessageState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edge("agent", "tools", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        
        self.graph = graph_builder.compile()
        return self.graph
    
    
    def __call__(self):
        pass