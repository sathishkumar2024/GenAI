"""
Docstring for chatbot.chatbot
    1. prompt -- define system and user 
    2. model
    3. output parse
    4. invoke
    
"""



from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 
import os
from dotenv import load_dotenv
from openai import RateLimitError

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistance. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)


st.title("first chat bot")

input_text = st.text_input("Search the topic u want")

llm = ChatOpenAI(model = "gpt-4o-mini")

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    try:
        st.write(chain.invoke({"question": input_text}))
    
    except RateLimitError:
        print("⚠️ OpenAI quota exceeded. Please check billing.")
    
    