from langchain_core.prompts import  PromptTemplate


#TODO 注意：prompt 模板的拼接，第一个必须为Prompt模板
prompt = (
    PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
    + ",让我开心下"
    + "\n 使用{language}语言"
    + PromptTemplate.from_template("\n 笑话要足够冷哈")
)

print(prompt.format(subject="AI", language="中文"))
