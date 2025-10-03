import  dotenv
from dotenv import load_dotenv, find_dotenv

from openai import OpenAI

from utils import output_json

# 导入配置文件
_ = load_dotenv(find_dotenv())



# 自定义混合缓冲记忆类，实现以下功能
# 1.max_tokens用于判断是否需要生成新的摘要
# 2.summary用于存储摘要的信息
# 3.chat histories用于存储历史对话
# 4.get_num_tokens用于计算传入文本的token数
# 5.save_context用于存储新的交流对话
# 6.get_buffer_string用于将历史对话转换成字符串
# 7.load_memory_variables用于加载记忆变量信息
# 8.summary_text用于将旧的摘要和传入的对话生成新摘要

class ConversationSummaryBufferMemory:
    def __init__(self,summary: str = "", chat_histories: list=[], max_token: int = 300):
        self.summary = summary
        self.chat_histories = chat_histories
        self.max_token = max_token
        self.client = OpenAI()

    def get_num_tokens(self,text: str) -> int:
        '''用于计算传入文本的token数'''
        return len(text)

    def save_context(self,human_query: str, ai_content: str):
        '''用于存储新的交流对话'''
        self.chat_histories.append({'Human': human_query, 'AI': ai_content})

        # TODO 这里需要循环检测是否需要生成新的摘要
        while True:
            chartTxt = self.get_buffer_string()
            # print("当前对话长度：",self.get_num_tokens(chartTxt),"内容为：\n"+chartTxt)
            if self.get_num_tokens(chartTxt) > self.max_token:
                print("需要生成新的摘要...")
                first_chat = self.chat_histories[0]
                self.summary = self.summary_text(self.summary, f'Human:{first_chat.get("Human")}\nAI:{first_chat.get("AI")}')

                print("新摘要：",self.summary)
                del self.chat_histories[0]
            else:
                break
    def get_buffer_string(self):
        '''将历史对话转换成字符串'''
        return "\n\n".join([f"Human:{i['Human']}\nAI:{i['AI']}" for i in self.chat_histories])

    def load_memory_variables(self)-> dict:
        '''用于加载记忆变量信息'''
        buffer_string = self.get_buffer_string()
        return {
            "chat_history": f"摘要：{self.summary }\n\n历史对话：{buffer_string}\n\n"
        }

    def summary_text(self,original_summary: str,new_line: str = "") -> str:
        '''将旧的摘要和传入的对话生成新摘要'''
        prompt =f''' 你是一个强大的聊天机器人，请根据用户的谈话内容和摘要信息，返回一个新的摘要。摘要示例<example>z中的内容不参与摘要汇总，只要汇总，不要推理，并且只返回新的摘要内容。

摘要示例：
<example>
当前摘要： 用户正在计划去北京出差，之前已经确定了出发日期是10月15日，但还没有订机票。

新的对话：
Human：帮我查一下从上海到北京10月15号上午的航班。
AI：有两班直飞航班比较合适：
    - 08:00 起飞，09:55 到达，价格 850 元。
    - 10:00 起飞，11:55 到达，价格 780 元。
Human：我更想早点到，那就选 08:00 的吧。

新摘要：用户正在计划10月15日从上海出发去北京出差，目前已决定预订 08:00 的直飞航班（09:55 抵达），票价约 850 元。
</example>


当前摘要： {original_summary}

新的对话列表：{new_line}

请将以上内容按要求生成摘要。
        '''

        resp = self.client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        return resp.choices[0].message.content
    def clear(self):
        '''用于清空历史对话'''
        self.chat_histories = []





# 创建OpenAI客户端
client = OpenAI()
memory = ConversationSummaryBufferMemory("", [], 300)

# 命令行模拟对话
while True:
    user_input = input("Human：")
    if user_input == "":
        break

    variables = memory.load_memory_variables()
    answer_prompt = (
        f"你是一个强大的聊天机器人，请根据上下文和用户提问回答问题。\\n",
        variables.get("chat_history"),
        f"用户提问是:{user_input}",
    )
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            # {"role": "system", "content": "你是一个OpenAI聊天机器人，帮助用户回答问题。"},
            # {"role": "user", "content": "\n".join(answer_prompt)},
            {"role": "user", "content": answer_prompt},
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
    # 保存对话
    memory.save_context(user_input, ai_content)

    print("")

    print(f"\n\n最新摘要:{memory.summary}\n 对话历史：")
    output_json(memory.chat_histories)