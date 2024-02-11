from __future__ import annotations
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
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


if __name__ == "__main__":
    
    
    load_dotenv()

    llm = ChatOpenAI(
            model = "gpt-3.5-turbo",
            openai_api_key = os.getenv("API_KEY"), 
            temperature= 0.7
        )
    
    ob = AssessmentMCQ(
        llm = llm,  
        output_parser= StrOutputParser(),
    )

        
    data = {
            "topic": "JavaScript Regular Expression",
            "summary": """A regular expression is a sequence of characters that forms a search pattern.

            The search pattern can be used for text search and text replace operations.

            What Is a Regular Expression?
            A regular expression is a sequence of characters that forms a search pattern.

            When you search for data in a text, you can use this search pattern to describe what you are searching for.

            A regular expression can be a single character, or a more complicated pattern.

            Regular expressions can be used to perform all types of text search and text replace operations.

            Syntax
            /pattern/modifiers;
            Example
            /w3schools/i;
            Example explained:

            /w3schools/i  is a regular expression.

            w3schools  is a pattern (to be used in a search).

            i  is a modifier (modifies the search to be case-insensitive).

            Using String Methods
            In JavaScript, regular expressions are often used with the two string methods: search() and replace().

            The search() method uses an expression to search for a match, and returns the position of the match.

            The replace() method returns a modified string where the pattern is replaced.

            Using String search() With a String
            The search() method searches a string for a specified value and returns the position of the match:

            Example
            Use a string to do a search for "W3schools" in a string:

            let text = "Visit W3Schools!";
            let n = text.search("W3Schools");
            The result in n will be:

            6

            Using String search() With a Regular Expression
            Example
            Use a regular expression to do a case-insensitive search for "w3schools" in a string:

            let text = "Visit W3Schools";
            let n = text.search(/w3schools/i);
            The result in n will be:

            6

            Using String replace() With a String
            The replace() method replaces a specified value with another value in a string:

            let text = "Visit Microsoft!";
            let result = text.replace("Microsoft", "W3Schools");
            Use String replace() With a Regular Expression
            Example
            Use a case insensitive regular expression to replace Microsoft with W3Schools in a string:

            let text = "Visit Microsoft!";
            let result = text.replace(/microsoft/i, "W3Schools");
            The result in res will be:

            Visit W3Schools!
            Did You Notice?
            Regular expression arguments (instead of string arguments) can be used in the methods above.
            Regular expressions can make your search much more powerful (case insensitive for example).""",
                    "sources": [
                        {
                            "title": "SourceTitle1",
                            "link": "SourceLink1"
                        },
                        {
                            "title": "SourceTitle2",
                            "link": "SourceLink2"
                        },
                        {
                            "title": "SourceTitle3",
                            "link": "SourceLink3"
                        }
                    ],
                    "code": "YourCode",
                    "youtube": [
                        {
                            "title": "VideoTitle1",
                            "link": "VideoLink1",
                            "timestamp": "Timestamp1"  # Replace with actual timestamp or set to None
                        },
                        {
                            "title": "VideoTitle2",
                            "link": "VideoLink2",
                            "timestamp": None
                        },
                        {
                            "title": "VideoTitle3",
                            "link": "VideoLink3",
                            "timestamp": "Timestamp3"
                        }
                    ]
                }
    
    parameter = ob.prompt_parameter_parser(data = data, language_type="javascript", question_level="easy")
    response = ob.utility_context_mcq_chain_generation(parameter=parameter)

    print(response)

    # ob.process_json(json_data = json_response)


# Create pipeline to store the data in the JSON object
# Work on the file generation and the unit test cases
    # Provide the data, and parameters, and test the result generated

# Work on the game design for MCQ gameplay, and keep check on the difficulty level of the questions
    
# Design the boiler plate for the DOCKERFILE, and decide the containers we will be using
# Design the prompt we will be needing to add the requirements file for the container,
# Make the bash file to run it directly in the container terminal 
# Test on the working of the container, and output generation
    
# Create a mini webpage to test the agents and the output it is providing. : Use Streamlit