import dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

#编排prompt
joke_prompt = ChatPromptTemplate.from_template('请讲一个关于{subject}的冷笑话')
poem_prompt = ChatPromptTemplate.from_template('请讲一个关于{subject}的诗')

# 创建大语言模型
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

# 创建解析器
parser = StrOutputParser()

# 编排chain
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 创建RunnableParallel
# map_chain = RunnableParallel({
#     "joke": joke_chain,
#     "poem": poem_chain,
# })

map_chain = RunnableParallel(joke=joke_chain, poen=poem_chain)


res = map_chain.invoke({
    "subject": "程序员"
})

print(res)








