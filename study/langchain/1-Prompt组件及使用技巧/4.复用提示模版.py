from langchain_core.prompts import PromptTemplate,PipelinePromptTemplate

full_template = PromptTemplate.from_template(
    """
    {instruction}
    
    {example}
    
    {start}
    """
)

instruction_template = PromptTemplate.from_template("你正在模拟{Person}")

example_template = PromptTemplate.from_template(
    """
    Q: {example_q}
    A: {example_a}
    """
)

start_template = PromptTemplate.from_template(
    """
    现在你是一个真实的人，请回答用户的问题：
    Q: {input}
    A: 
    """
)

pipeline_prompts =[
        ("instruction", instruction_template),
        ("example", example_template),
        ("start", start_template),
]

pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_template,
    pipeline_prompts=pipeline_prompts,
)

print(pipeline_prompt.invoke({
    "Person": "雷军",
    "example_q": "你最喜欢的汽车是什么？",
    "example_a": "小米su7",
    "input": "你最喜欢的手机是什么？",
}).to_string())

