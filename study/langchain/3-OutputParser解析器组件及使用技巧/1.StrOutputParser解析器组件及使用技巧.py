from dotenv import load_dotenv,find_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import  BaseModel,Field

# 导入配置文件
_ = load_dotenv(find_dotenv())


# 创建llm
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

# 创建输出解析器
#定一个json数据结构，告诉0penAI的输出解析器，如何解析
class Joke(BaseModel):
    joke: str = Field(description="回答用户冷笑话")
    punchline: str = Field(description=" 这个冷笑话的笑点")

parser = JsonOutputParser(pydantic_object=Joke)

# 创建prompt
prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instruction}\n{query}")\
    .partial(format_instruction=parser.get_format_instructions())


# print(prompt.format(query="讲一个关于教师的冷笑话"))
# 调用
content = parser.invoke(llm.invoke(prompt.invoke({"query": "讲一个关于教师的冷笑话"})))

print(content)

