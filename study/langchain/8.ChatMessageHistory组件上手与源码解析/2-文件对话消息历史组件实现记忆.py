import  dotenv
from dotenv import load_dotenv, find_dotenv

from openai import OpenAI
from langchain_community.chat_message_histories import FileChatMessageHistory

# 导入配置文件
_ = load_dotenv(find_dotenv())



# 创建OpenAI客户端
client = OpenAI()
chat_history = FileChatMessageHistory("./memery.txt")

# print(chat_history)

# 命令行模拟对话
while True:
    user_input = input("Human：")
    if user_input == "":
        break

    system_prompt = f'''
        你是一个强大的聊天机器人，请根据上下文和用户提问回答问题。\n\n
        <context>{chat_history}</context>
    '''

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        stream=True,
    )

    # print(response.choices[0].message.content)

    print("AI:", end="", flush=True)
    ai_content = ""
    for chunk in response:
        if chunk.choices and len(chunk.choices) > 0:
            content = chunk.choices[0].delta.content
            if content is None:
                break
            if content:
                print(content, end="", flush=True)
                ai_content += content
    chat_history.add_user_message(user_input)
    chat_history.add_ai_message(ai_content)
    print("")
