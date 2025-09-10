from langchain_core.prompts import  ChatPromptTemplate

system_prompt = ChatPromptTemplate.from_messages([
    "system", "你是OpenAI的开发聊天机器人,请根据用户的提问进行回复，我叫{username}"
])
human_prompt = ChatPromptTemplate.from_messages([
    "human", "{question}"
])

chat_prompt = system_prompt + human_prompt
print(chat_prompt.invoke({
    "username": "goen88",
    "question": "你叫什么名字？"
}).to_string())
