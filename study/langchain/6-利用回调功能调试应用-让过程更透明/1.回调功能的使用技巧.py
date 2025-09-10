import time
from typing import Any, Optional, Union
from uuid import UUID

import dotenv
from langchain_core.messages import BaseMessage
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk, LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler

dotenv.load_dotenv()


# 自定义回调
class MyCallbackHandler(BaseCallbackHandler):
    """自定义Callback处理器"""

    start_at:float = 0
    def on_chat_model_start(
        self,
        serialized: dict[str, Any],
        messages: list[list[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        self.start_at = time.time()
        print("开始调用大语言模型")
        print("序列化配置信息：",serialized)
        print("messages：",messages)

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        end_at = time.time()
        print("response:",response)
        print("耗时：",end_at-self.start_at)

    def on_llm_new_token(
        self,
        token: str,
        *,
        chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        print("正在生成Token：",token)


#编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 创建大语言模型
llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

# 创建解析器
parser = StrOutputParser()

# 构建链
chain = {"query": RunnablePassthrough()} | prompt | llm | parser

# 调用链并执行
content = chain.stream('你好，我是谁？',config={"callbacks":[StdOutCallbackHandler(),MyCallbackHandler()]})  # 直接传递字符串
# content = chain.invoke('你好，我是谁？',config={"callbacks":[StdOutCallbackHandler(),MyCallbackHandler()]})  # 直接传递字符串

# print(content)
for chunk in content:
    pass
    # print(chunk)










