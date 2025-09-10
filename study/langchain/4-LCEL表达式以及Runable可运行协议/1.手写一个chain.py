from typing import Any

from dotenv import load_dotenv,find_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import  StrOutputParser

_ = load_dotenv(find_dotenv())

#1、构建组件
prompt = ChatPromptTemplate.from_template('{query}')
llm = ChatOpenAI(model_name='gpt-3.5-turbo-16k')
strParser = StrOutputParser()


# 定义一个链
class Chain:
    steps: list = []

    def __init__(self,steps: list):
        self.steps = steps

    def invoke(self,input: Any):
        for step in self.steps:
            input = step.invoke(input)
        return input

# 编排链
chain = Chain([prompt,llm,strParser])

# 输出
print(chain.invoke({'query':'请根据用户的提问进行回复.\n如何使用langchain?'}))