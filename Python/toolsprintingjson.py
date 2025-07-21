from pydantic import BaseModel
import json
import os
import wikipedia
import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class ToolOutput(BaseModel):
    tool_name: str
    result: str

class ExplanationOutput(BaseModel):
    tool_name: str = "Explanation"
    result: str



def arthemati_tool(query: str) -> str:
    try:
        result = float(eval(query))
    except Exception:
        result = "Expression is not correct"
    return ToolOutput(tool_name="Calculator", result=str(result)).json()

def datetime_tool() -> str:
    now = datetime.datetime.now()
    return ToolOutput(tool_name="Current_date_time", result=str(now)).json()

def searchig_wikiedia(query: str) -> str:
    try:
        result = wikipedia.summary(query, sentences=4)
    except Exception:
        result = "We can't search on Wikipedia"
    return ToolOutput(tool_name="Wikipedia", result=result).json()

def python_tool(code: str) -> str:
    try:
        result_dict = {}
        exec(code, {}, result_dict)
        result = str(result_dict)
    except Exception as e:
        result = str(e)
    return ToolOutput(tool_name="ProgramExecution", result=result).json()



def getting_output(user_input):
  
    math_tools = [Tool(name="Calculator", func=arthemati_tool,
                       description="Handles all mathematical operations")]
    
    info_tools = [
        Tool(name="Wikipedia", func=searchig_wikiedia,
             description="Searches for information on Wikipedia"),
        Tool(name="Current_date_time", func=datetime_tool,
             description="Returns the current date and time")
    ]

    exce_tools = [Tool(name="ProgramExecution", func=python_tool,
                       description="Executes Python code and returns result")]


    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.6)

    agent_math = initialize_agent(
        tools=math_tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    agent_info = initialize_agent(
        tools=info_tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    agent_python = initialize_agent(
        tools=exce_tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True
    )


    if any(p in user_input.lower() for p in ["add", "subtract", "multiply", "divide", "modulo", "+", "-", "/", "*", "%", "**", "power"]):
        return agent_math.run(user_input)
    
    elif any(p in user_input.lower() for p in ["detailed", "explain", "date", "time", "wiki"]):
        return agent_info.run(user_input)
    
    elif "python" in user_input.lower() or "code" in user_input.lower():
        return agent_python.run(user_input)
    
    else:
        prompt = PromptTemplate(
            template="Explain the content in 100 to 200 words for a beginner user. {user_input}",
            input_variables=["user_input"]
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(user_input)
        return ExplanationOutput(result=response).json()


if __name__ == "__main__":
    ip = input("Enter your Prompt: ")
    output = getting_output(ip)
    print(json.dumps(json.loads(output), indent=1))  
