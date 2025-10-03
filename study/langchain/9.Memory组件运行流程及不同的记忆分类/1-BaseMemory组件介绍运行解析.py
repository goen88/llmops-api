# from langchain.chains.llm import LLMChain
# from langchain_core.memory import BaseMemory
from langchain.memory.chat_memory import BaseChatMemory

#以下是伪代码
memory  = BaseChatMemory(
    input_key="query",
    output_key="output",
    return_messages=True,
    # chat_history 假设
)

memory_variable = memory.load_memory_variables({})

# content = chain.invoke({"query": "请根据用户的提问进行回复.\n请讲一个关于程序员的笑话?","chat_history":memory_variable.get("chat_history")})
# memory.save_context({"human": "请根据用户的提问进行回复.\n请讲一个关于程序员的笑话?"},{"output": content})
