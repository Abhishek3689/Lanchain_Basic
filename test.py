# import langchain
# import openai
import os
from langchain.llms import openai
#from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
#from langchain.prompts import PromptTemplate

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv('openai_key')
llm=openai.OpenAI(temperature=.6)

#llm=OpenAI(temperature=.6)

st.title("This is Home Page for LLM Open AI")
input_text=st.text_input("Enter the topic you want to search")



if input_text:
    st.write(llm(input_text))