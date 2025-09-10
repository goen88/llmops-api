import dotenv
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()


def retrieval(query:str) -> str:
    """
    定义一个模拟检索器函数
    """
    print(f"正在检索：{query}")
    return "我是Goen88，一名AI工程师。"



#编排prompt
prompt = ChatPromptTemplate.from_template('''请根据用户的问题回答，可以参考上下文进行生成

<context>
{content}
</context>

用户的问题是：{query}''')

# 创建大语言模型
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

# 创建解析器
parser = StrOutputParser()

# 构建链
# chain = RunnableParallel({
#     "content": lambda x: retrieval(x['query']),
#     "query": itemgetter('query')
# }) | prompt | llm | parser
# 也可用间写的方式，因为连中可以自动将字典转成Runnable
chain = {
    "content": lambda x: retrieval(x['query']),
    "query": itemgetter('query')
} | prompt | llm | parser



# 调用链
#content = chain.invoke({'content': retrieval('你好，我是谁？'), 'query': '你好，我是谁？'})
content = chain.invoke({'query': '你好，我是谁？'})

print(content)










