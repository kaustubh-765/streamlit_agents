from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
import json
from pydantic import BaseModel


class Prompt_parameter(BaseModel):
    language_type :str
    question_level : str
    topic: str
    summary: str


class Assessment:
    def __init__(self, llm, output_parser) -> None:
        self.llm = llm
        self.output_parser = output_parser
        
    def __generating_series_prompt(self):
        self.prompt = ChatPromptTemplate.from_messages([
                        ("system", "You are a professor of {topic}, and you are responsible for generating unique Easy, Medium ,or Hard level programming problems, level will be mentioned below."),
                        ("user", """Generate a DSA coding task/assignment applicable to language/framework mentioned below.
                            The Task should be independent and solvable on it's own. 

                            Language: {language_type}
                            Level: {question_level}

                            Also, find attach the summary of the topic, and generate problems with context to the topic title and the summary provided below. 
                            
                            Summary: {summary}

                            The structure of the response should be of the form: 

                            Task: This should contain the problem statement, and should be a detailed explanation of the requirement of the programming problem.

                            Function Signature: The response should also consist of function signature in which the user will do the implementation.

                            Examples: The response should also consist of minimum of three examples to provide the user with the type of input required, and output expected
                                    and should also explain how the output is achieved giving the hint of the implementation of the problem.
                                    The Examples should contain following headings: ['Input', 'Output', 'Explanation'].

                            Constraints: The response should also consist the set of constraints applicable on the problem.

                            Sample Solution: Provide a working solution for the generated task that follows coding best practices. 
                                            The solution should be implemented in the specified language/framework. 

                            Unit Test Generation: Generate five unit tests for the generated task in the {language_type} programming language using tesing techniques from the language. 
                                                These tests should ensure correctness and reliability of the solution. 
                                                The unit tests generation should contain one single function in the language under the heading.

                            The above list of headings, should be the format of the response. Generate the JSON response where each heading is the key and their required output is the content in the JSON file, the content of the keys should be strings written using markdown instructions.""")
                        ])



    def __generating_chain(self, parameter: Prompt_parameter) -> str:
        self.__generating_series_prompt()
        chain = self.prompt | self.llm | self.output_parser
        response = chain.invoke(parameter.dict())
        
        return response
    
    def utility_context_chain_generation(self, language_type, question_level, rspns_gene_agnt:json):

        topic = rspns_gene_agnt['topic'] if 'topic' in rspns_gene_agnt else "Data Structure and Algorithm"
        summary = rspns_gene_agnt['summary'] if 'summary' in rspns_gene_agnt else "Does not exists."

        prompt_parameters = Prompt_parameter(
            language_type=language_type,
            question_level=question_level,
            topic=topic,
            summary=summary
        )

        response = self.__generating_chain(prompt_parameters)

        return response
    
    def json_response_generation(self, response:str):
        return json.loads(response)
    
        
    def __write_to_file(self, heading, content):
        with open(f"{heading.replace(' ', '_')}.txt", "w") as file:
            file.write(content)

    def process_json(self, json_data):
        for heading in ["Task", "Function Signature", "Examples", "Constraints", "Sample Solution", "Unit Test Generation"]:
            if heading in json_data:
                content = json_data[heading]
                if heading == "Examples" or heading == "Unit Test Generation":
                    examples_content = ""
                    for example in content:
                        input_data = example.get("Input", "")
                        output_data = example.get("Output", "")
                        explanation = example.get("Explanation", "")
                        example_content = f"Input: {input_data}\nOutput: {output_data}\nExplanation: {explanation}\n\n"
                        examples_content += example_content
                    self.__write_to_file(heading, examples_content)
                else:
                    self.__write_to_file(heading, content)

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
