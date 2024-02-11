# app.py
import streamlit as st
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os 
from coding_problem_generator import Assessment
from mcq_problem_generator import AssessmentMCQ
from unit_test_cases_dataset import data

# Create the pages
def page1():
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

def page2():
    st.title("Testing MCQ Assesment Generator")

    param1 = st.text_input("Enter Language")
    param2 = st.text_input("Enter difficulty level")

    option = st.selectbox('Select an option', (0, 1, 2, 3, 4, 5))
    st.text(data[option])


    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
        openai_api_key = os.getenv("API_KEY")
    )

    ob = AssessmentMCQ(llm=llm, output_parser=StrOutputParser())
        

    if st.button("Submit"):
        parameter = ob.prompt_parameter_parser(language_type=param1, question_level=param2, data=data[option])
        response = ob.utility_context_mcq_chain_generation(parameter=parameter)
        st.text(response)

def main():
    st.title("Multi-Page App with Navigation Bar")

    # Create a sidebar as a navigation bar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Coding Assessment", "MCQ Assessment"])

    if selection == "Home":
        st.write("Welcome to the app")
    elif selection == "Coding Assessment":
        page1()
    elif selection == "MCQ Assessment":
        page2()

if __name__ == "__main__":
    main()
