import sys
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

class MCQAssessmentGetter:
    """Class to generate MCQ questions for the problem"""
    def __init__(self, temperature ,parameter: AssessmentPromptParameter, memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)) -> None:
        """
            Initialize the prompt to be used and the chain 

            Args:
                parameter(AssessmentPromptParameter): Prompt parameters

        """
        prompt_factory = PromptFactory(prompt_parameter=parameter, prompt_string="")
        prompt = prompt_factory.generate_mcq_assessmemt_prompt()
        self.chain = ChainFactory(prompt=prompt, human_input="Generate the assessment.", memory = memory, temperature=temperature)
        

    def get_mcq_assessment(self):
        """
            Function to generate the MCQ assessment.
        """

        response = self.chain.initialize_agent()
        transform = OutputTransformer(response)
        response = transform.transform()

        return response
    

# if __name__ == "__main__":

#     query = "list comprehension in python"
#     parameter = AssessmentPromptParameter(
#         language_type="Python",
#         question_level="Easy",
#         summary="",
#         topic=query
#     )

#     mcq = MCQAssessmentGetter(parameter=parameter)
#     content = mcq.get_mcq_assessment()
#     print(content)
