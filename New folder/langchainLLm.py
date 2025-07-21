from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
from langchain.chat_models import init_chat_model
from langchain_community.retrievers import WikipediaRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

from langsmith import traceable


retriever = WikipediaRetriever()


faiss_db = None


if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBzM8OxfOtVaB42USu5WLx7aR_hsqOPGjM"


llm = init_chat_model("gemini-1.5-flash", model_provider="google_genai")


splitter = RecursiveCharacterTextSplitter(chunk_size=1200 , chunk_overlap=100)

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def context_retriving(user_input):
    document_text = retriever.invoke(user_input)  
    print("This is the wikipedia context")
    print(document_text)
    documents = splitter.split_documents(document_text)
    return list(documents)


def docs_format(user_input):
    docs = context_retriving(user_input)
    return [doc.page_content for doc in docs]


def storing_in_vectore_db(user_input):
    global faiss_db
    documents = context_retriving(user_input)
    faiss_db = FAISS.from_documents(documents=documents, embedding=embedding)

#this traceable is used to track the application
@traceable
def query_reply(user_input):
    global faiss_db
    if faiss_db is None:
        storing_in_vectore_db(user_input)  
    context_docs = faiss_db.similarity_search(user_input, k=3)
    context = [doc.page_content for doc in context_docs]

    prompt = ChatPromptTemplate.from_template("""
    Explain the topic in 300 word  like a expert 
    Context: {context}
    Question: {question}
    """)

    chain = (
        {
            "context": lambda _: context,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    retext = chain.invoke({"question": user_input})
    return retext

t = input("Enter your question: ")
ou = query_reply(t)
print("Answer:", ou)
