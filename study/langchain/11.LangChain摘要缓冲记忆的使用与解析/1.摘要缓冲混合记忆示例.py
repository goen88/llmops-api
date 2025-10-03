from operator import itemgetter

from dotenv import find_dotenv,load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory

# from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint

_ = load_dotenv(find_dotenv())

# 创建prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI的开发聊天机器人，请根据对应的上下文，回复用户问题。"),
    MessagesPlaceholder("history"),
    ("human", "{query}"),
])

# 创建memory
memory = ConversationSummaryBufferMemory(
    max_token_limit=300,
    llm=ChatOpenAI(model="gpt-3.5-turbo-16k"),
    input_key="query",
    return_messages=True,
)

# 创建llm
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
# llm = QianfanChatEndpoint()

# 创建输出解析器
parser = StrOutputParser()

# chain
# 写法1
# memory_variable = memory.load_memory_variables({})
# RunnablePassthrough.assign(history=lambda x: memory_variable.get("history"))


chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | parser

while True:
    query = input("Human:")
    if query == "":
       continue
    if query == "q":
        exit(0)
    # 创建chain输入
    chain_input = {"query": query}

    # 执行chain，采用流式输出
    response = chain.stream(chain_input)
    print("AI:", end="", flush=True)

    output = ""
    for chunk in response:
        output += chunk
        print(chunk, end="", flush=True)

    memory.save_context(inputs=chain_input, outputs={"output": output})
    print( "")
    print(f"历史消息: ", memory.load_memory_variables({}))





