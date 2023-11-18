# import langchain
# import openai
import os
from langchain.llms import openai
import streamlit as st
from langchain.prompts import PromptTemplate
from constants import openai_key

os.environ["OPEN"]
st.title("This is Home Page for LLM Open AI")
st.text_input("Enter the topic you want to search")

