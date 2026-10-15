
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=100
)

response =llm.invoke("who is lord Ram")
print(response.content)
