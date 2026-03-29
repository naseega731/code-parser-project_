from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def get_ai_feedback(code):
    prompt = f"Analyze this Python code and give suggestions:\n{code}"
    response = llm.invoke(prompt)
    return response.content
