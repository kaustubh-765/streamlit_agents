from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os

class ChainFactory:

    def __init__(
            self,
            prompt,
            temperature = 0,
            output_transformer = StrOutputParser,
            model = "gpt-3.5-turbo",
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True),
            human_input = ""
        ):

        self.prompt = prompt
        self.output_transformer = output_transformer
        self.memory = memory
        self.llm = ChatOpenAI(
            model = model,
            openai_api_key = os.getenv("API_KEY"), 
            temperature= temperature
        )
        self.human_input = human_input
        

    def initialize_agent(self):

        self.llm_chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=True,
        )

        response = self.llm_chain.predict(human_input = self.human_input)

        return response