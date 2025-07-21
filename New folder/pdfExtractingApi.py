from fastapi import FastAPI ,File ,UploadFile  
from langchain_core.output_parsers import  StrOutputParser
from  langchain_google_genai import GoogleGenerativeAIEmbeddings , ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from  langchain_core.runnables import RunnablePassthrough 
import os
from dotenv import load_dotenv
from PIL import Image 
import pytesseract
from pydantic import Field, FileUrl,BaseModel
from cv2 import cv
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter




faiss_db =None

app=FastAPI()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap =100)
class PdfFileFormate(BaseModel):
    titel : str
    description: str



load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

os.environ("GOOGLE_API_KEY") = google_api_key

llm = ChatGoogleGenerativeAI(model ="gemini-1.5-flash",temperature=1.4)

parser  = StrOutputParser()

embedding  = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


def extracting_the_text(image):
   img = Image.open(image)
   text_extracting = pytesseract.image_to_string(img)
   documents = splitter.split_documents(text_extracting)
   return list(documents)

def docs_format(filee):
    docs = extracting_the_text(filee)
    return [doc.page_content for doc in docs]


def storing_in_vectore_db(user_input):
    global faiss_db
    documents = context_retriving(user_input)
    faiss_db = FAISS.from_documents(documents=documents, embedding=embedding)


@app.post("/UploadingPDF")
def Uploading_pdf_for_qa(fdata :PdfFileFormate,
         file: UploadFile = File(..., description="Upload an pdf file under 10MB .pdf")):
   extracted_text = extracting_the_text(file)
   


