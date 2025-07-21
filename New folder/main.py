from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel 
import os 
import logging
from langchain_core.output_parsers import StrOutputParser

logger = logging.getLogger(__name__)


load_dotenv()

app = FastAPI()

class  InputData(BaseModel):
    query : str 
    username :str

google_api_key  = os.getenv("GOOGLE_API_KEY")   

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = google_api_key

llm = ChatGoogleGenerativeAI(model ="gemini-2.0-flash", temperature = 0.9)    

@app.post("/sending_query")
def sending_querythe(query:InputData):
    
    prompt = PromptTemplate(
    template="Explain the topic in 100 words in pointwise manner like you are the expert of that particular field: {query}",
    input_variables=["query"]
         )
    
    chain = prompt | llm | StrOutputParser()
    use = query.username
    logger.info("The username who request the query {}",use)
    text_out = chain.invoke(query)
    return text_out




if __name__ == "__main__":
  app.run()
#eve
