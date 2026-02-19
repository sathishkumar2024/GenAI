import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import sys
st.write(sys.executable)

load_dotenv()



os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT") 


# Prompt Template
prompt = ChatPromptTemplate(
    [
        
        ("system", "You are a helpfull assitant. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)


st.title("Langchain demo with Gemma")
input_text = st.text_input("What question you have in mind?")

llm = Ollama("gemma")

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
