import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
from coding_problem_generator import Assessment
from unit_test_cases_dataset import data

st.title("Testing Assesment Generator")

param1 = st.text_input("Enter Language")
param2 = st.text_input("Enter difficulty level")

option = st.selectbox('Select an option', (0, 1, 2, 3, 4, 5))
st.text(data[option])

llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    openai_api_key = os.getenv("API_KEY")
)

ob = Assessment(llm=llm, output_parser=StrOutputParser())

if st.button("Submit"):
    response = ob.utility_context_chain_generation(language_type=param1, question_level=param2, rspns_gene_agnt=data[option]) 
    st.text(response)
