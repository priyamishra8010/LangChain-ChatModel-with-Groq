# import os
# from dotenv import load_dotenv

# load_dotenv()
# # os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
# from langchain_groq import ChatGroq
# # from langchain.agents import create_agent
# # from langchain_community.tools import DuckDuckGoSearchRun

# from groq import Groq

# client = Groq()

# models = client.models.list()

# for model in models.data:
#     print(model.id)


# # 1. Groq LLM
# llm = ChatGroq(
#     model="qwen/qwen3.8-27b",
#     temperature=0
# )

# response=llm.invoke("who is lord Hanuman? ")
# print(response.content)




#practice

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