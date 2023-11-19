# import langchain
# import openai
import os
from langchain.llms import openai
import streamlit as st
from langchain.prompts import PromptTemplate
from constants import openai_key

os.environ["OPENAI_API_KEY"]=openai_key 
st.title("This is Home Page for LLM Open AI")
input_text=st.text_input("Enter the topic you want to search")

llm=openai(temperature=.8)

if input_text:
    st.write(llm(input_text))