from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from fastapi import FastAPI
import uvicorn
import openai
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()
OpenAI()
# llm = OpenAI(
#     model_name="gpt-4",
#     temperature=0,
#     openai_api_key=os.environ['OPENAI_API_KEY']
#     )
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=os.environ['OPENAI_API_KEY']
)

@app.get('/ask-llm')
def ask_llm(query: str):
    res = llm.predict(query)
    print(res)
    return res

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=True)