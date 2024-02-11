from __future__ import annotations
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
import json
from pydantic import BaseModel, ConfigDict, ValidationError
from typing import List


class MCQ(BaseModel):
    model_config = ConfigDict(strict=True)

    Task: str
    Multiple_choice: List[str]
    Correct_answer: str


class Prompt_parameter(BaseModel):
    language_type :str
    question_level : str
    topic: str
    summary: str


class AssessmentMCQ:
    def __init__(self, llm, output_parser) -> None:
        self.llm = llm
        self.output_parser = output_parser

    def __generating_series_prompt(self):
        self.prompt = ChatPromptTemplate.from_messages([
                        ("system", "You are a professor of {topic}, and you are responsible for generating unique Easy, Medium ,or Hard level multiple choice problems, level will be mentioned below."),
                        ("user", """Generate a multiple choice questions applicable to language/framework mentioned below.
                            The Task should be independent and solvable on it's own. 

                            Language: {language_type}
                            Level: {question_level}

                            Also, find attach the summary of the topic, and generate questions with context to the topic title and the summary provided below, you can also use your knowledge base to generate unique questions. 
                            
                            Summary: {summary}

                            The structure of the response should be of the form: 

                            Task: This should contain the problem statement, and should be a detailed explanation of the requirement of the multiple choice question.

                            Multiple_choice: This should contain the list of the possible answers where out of all only one is correct, Generate atleast 4 - 5 possible answers.

                            Correct_answer: This should contain the correct answer out of the provided possible answers in the above tag.

                            The above list of headings, should be the format of the response. Generate the JSON response where each heading is the key and their required output is the content in the JSON file.""")
                        ])
        
    def __generating_chain(self, parameter: Prompt_parameter):
        if parameter.summary == None:
            return "Invalid Summary!"

        self.__generating_series_prompt()
        chain = self.prompt | self.llm | self.output_parser
        response = chain.invoke(parameter.dict())

        return response
    
   

    def prompt_parameter_parser(self, data: json, language_type: str, question_level:str):

        topic = data['topic'] if 'topic' in data else "Data Structure and Algorithm"
        summary = data['summary'] if 'summary' in data else ""

        return Prompt_parameter(
            language_type=language_type,
            question_level=question_level,
            topic=topic,
            summary=summary
        )
    
    def utility_context_mcq_chain_generation(self, parameter:Prompt_parameter):
        return self.__generating_chain(parameter=parameter)
    
    def generating_pydantic_model(self, response):

        try:
            # ob = MCQ.model_validate_json(response)
            question = MCQ.parse_raw(response)

        except ValidationError as e:
            print(e)

        return question
    
    def generating_end_assignment(self, parameter):
        response = self.utility_context_mcq_chain_generation(parameter=parameter)
        mcq_ass = self.generating_pydantic_model(response=response)

        return mcq_ass
        
    def store_json(self, json_data, file_path):
        """
        Stores a JSON object in a JSON file.

        Args:
        - json_data: JSON object to be stored.
        - file_path: Path to the JSON file where the data will be stored.

        Returns:
        - None
        """
        with open(file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
