from dotenv import load_dotenv,find_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 导入配置文件
_ = load_dotenv(find_dotenv())

# 创建prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 创建llm
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

# 创建输出解析器
strParser = StrOutputParser()
# print(strParser.parse("Hello World")) # 原来样输出

# 调用
content = strParser.invoke(llm.invoke(prompt.invoke({"query": "讲一个关于教师的冷笑话"})))

print(content)

