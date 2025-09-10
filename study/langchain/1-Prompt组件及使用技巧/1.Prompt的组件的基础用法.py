from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate,MessagesPlaceholder

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话！")

promptStr = prompt.format(subject="程序员")
print(promptStr)

invoke_prompt = prompt.invoke( {"subject": "喜剧演员"})
print(invoke_prompt.to_json())
print(invoke_prompt.to_string())
print(invoke_prompt.to_messages())

print("\n\n==ChatPromptTemplate用法===================================")

#ChatTemplate用法
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI的开发聊天机器人Goen88，清根据用的提问进行回复，当前的时间为：{now}"),
    #消息占位符, 用于存储聊天历史
    MessagesPlaceholder("chat_history"),
    ("human", "请讲一个关于{subject}的冷笑话")
])\
    #.partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # 使用partial 方法设置默认固定参数

# TODO 使用partial 方法设置默认固定参数(这样不生效)，partial 返回了一个新的 ChatPromptTemplate 对象，而不是修改原对象
# chat_prompt.partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 修改：partial之后，chat_prompt对象会改变，所以需要重新赋值给chat_prompt
chat_prompt = chat_prompt.partial(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#使用format_prompt方式
print("\n==使用format_prompt方式")
print(chat_prompt.format_prompt(
    subject="程序员",
    chat_history=[
        ("human", "你叫什么名字？"),
        AIMessage("你好，我叫Goen88"),
        HumanMessage("你能做什么？"),
        AIMessage("我什么都不能做，因为我是一个聊天机器人")
    ]).to_string()
)

# 使用invoke方式
print("\n==使用invoke方式")
print(chat_prompt.invoke({
    "subject": "喜剧演员",
    "chat_history": [
        ("human", "你叫什么名字？"),
        AIMessage("你好，我叫Goen88"),
        HumanMessage("你能做什么？"),
        AIMessage("我什么都不能做，因为我是一个聊天机器人")
    ]
}).to_messages())

