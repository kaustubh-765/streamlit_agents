import sys
import json
import warnings
from os.path import dirname, abspath

current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(parent_dir)

from OutputTransformer import OutputTransformer
from PromptFactory import PromptFactory
from ChainFactory import ChainFactory
from PromptParameter import AssessmentPromptParameter
from langchain.memory import ConversationBufferMemory

class CodeAssessmentGetter:
    """Class to generate coding assignments"""
    def __init__(self, temperature ,parameter: AssessmentPromptParameter, memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)) -> None:
        """
            Initialize the prompt to be used and the chain 

            Args:
                temperature(float): Temperature
                parameter(AssessmentPromptParameter): Prompt parameters
                memory(ConversationBufferMemory): ConversationBufferMemory 

        """
        prompt_factory = PromptFactory(prompt_parameter=parameter, prompt_string="")
        prompt = prompt_factory.generate_code_assessmemt_prompt()
        self.chain = ChainFactory(prompt=prompt, human_input="Generate the assessment.", memory = memory, temperature=temperature)
        

    def get_code_assessment(self):
        """
            Function to generate the coding assessment.
        """

        response = self.chain.initialize_agent()
        problems = json.loads(response)["problems"]
        problems = [json.dumps(problem) for problem in problems]
        return [OutputTransformer(problem).transform() for problem in problems]

# if __name__ == "__main__":

#     query = "list comprehension in python"
#     parameter = AssessmentPromptParameter(
#         language_type="Python",
#         question_level="Easy",
#         summary="",
#         topic=query
#     )

#     mcq = CodeAssessmentGetter(parameter=parameter, temperature=0.7, memory=ConversationBufferMemory(memory_key="chat_history"))
#     content = mcq.get_code_assessment()
#     print(content)
