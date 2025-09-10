from datetime import datetime

from dotenv import load_dotenv,find_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

# 导入配置文件
_ = load_dotenv(find_dotenv())


# 编排prompt
prompt = (ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI的开发聊天机器人Goen88，清根据用的提问进行回复，当前的时间为：{now}"),
    HumanMessagePromptTemplate.from_template("{query}")
])).partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 创建大语言模型

llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

ai_messages = llm.batch([
    prompt.invoke({"query": "你好，你是？"}),
    prompt.invoke({"query": "现在是几点?请将一个程序员工的冷笑话？"}),
])

for ai_message in ai_messages:
    print(ai_message.content)
    print("==============================")




