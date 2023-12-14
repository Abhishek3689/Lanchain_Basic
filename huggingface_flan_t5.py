import os

import streamlit as st
import langchain
from dotenv import load_dotenv
from langchain import HuggingFaceHub
#from constants.py import HUGGINGFACEHUB_TOKEN

load_dotenv()
os.environ['HUGGINGFACEHUB_API_TOKEN']=os.getenv('HUGGINGFACEHUB_TOKEN')

llm=HuggingFaceHub(repo_id='google/flan-t5-large',model_kwargs={'temperature':0.3,'max_length':64})



st.title("This is Home page of Langchain")
st.header("Welcome to Langchain")
input=st.text_input("Please ask the question")
res=llm(input)
st.write(res)
# if input=='abhi':
#     st.write("Enterd value is 1")
# else:
#     st.write("Enter value is different")
print("This is home page")