from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory,get_buffer_string

from utils import output_json

# BaseChatMessageHistory是抽象类，不能实例化
# chat_history = BaseChatMessageHistory()

inmemory_chat_history = InMemoryChatMessageHistory()
inmemory_chat_history.add_user_message("你好，我是人类")
inmemory_chat_history.add_ai_message("你好人类，我是openai机器人")

# print(inmemory_chat_history.messages)
print(get_buffer_string(inmemory_chat_history.messages))
