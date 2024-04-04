import sys
import warnings
from os.path import dirname, abspath

current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(parent_dir)

import streamlit as st
import json
from CodeAssessmentGetter import CodeAssessmentGetter
from PromptParameter import AssessmentPromptParameter
from langchain.memory import ConversationBufferMemory

global  language_type, difficulty_level, topic, summary, temperature, reset_memory

code_assessment_memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

if 'memory' not in st.session_state:
    st.session_state['memory'] = code_assessment_memory

def input_fields():
    
    global language_type, difficulty_level, topic, summary, temperature, reset_memory

    st.title("Testing Code Assesment Generator")

    language_type = st.text_input("Enter Language")
    difficulty_level = st.radio("Reset Memory", ["Easy", "Medium", "Hard"])
    topic = st.text_input("Enter the topic")
    summary = st.text_input("Enter the summary")
    temperature = st.slider("Enter the temperature for the LLM", 0.0, 1.0, 0.7)

    reset_memory = st.radio("Reset Memory", ["true", "false"])


def run_component():
    
    global language_type, difficulty_level, topic, summary, temperature, reset_memory

    if st.button("Submit"):

        if (reset_memory == "true"):
            code_assessment_memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
            st.session_state['memory'] = code_assessment_memory

        prompt_parameter = AssessmentPromptParameter(
            language_type=language_type,
            question_level=difficulty_level,
            topic=topic,
            summary=summary
        )

        mcq = CodeAssessmentGetter(parameter=prompt_parameter,  memory = st.session_state['memory'], temperature=float(temperature))
        content = mcq.get_code_assessment()

        content_type = {
            "data" : [
                {
                    "type": "assessment_type",
                    "value": "code"
                }
            ]
        }

            
        json_content = json.loads(content)
        json_content["data"].extend(content_type["data"])
        content = json.dumps(json_content, indent=4) 

        st.json(content)


st.set_page_config(
    page_title="Code Agent"
)
input_fields()
run_component()