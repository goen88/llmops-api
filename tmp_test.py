import time
import asyncio

from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.messages import  AIMessage,BaseMessage

async def get_messages():
    bch = InMemoryChatMessageHistory()
    bch.add_user_message("你好，我是人类")
    bch.add_ai_message("你好人类，我是openai机器人")
    tt = await bch.aget_messages()
    for i in tt:
        print(f'{i.type}:{i.content}')
    print(tt)

asyncio.run(get_messages())
