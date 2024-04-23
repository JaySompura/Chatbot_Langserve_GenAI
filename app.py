from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1 = ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"
)

add_routes(
    app,
    prompt1|model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)

