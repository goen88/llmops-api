import uuid
from dataclasses import dataclass

from flask import request,jsonify
from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import  OpenAI

from internal.model import App
from internal.schema import CompletionReq
from internal.service import AppService

from pkg.response import Response, HttpCode, validation_error_json, success_json, success_message, fail_message
from internal.exception import FailException

@inject
@dataclass
class AppHandler:
    '''
    应用控制器
     '''

    app_service:AppService

    def create_app(self):
        '''
        创建应用
        :return:
        '''
        app = self.app_service.create_app()
        return success_message(f"应用创建成功,id={app.id}")

    def get_app(self,id:uuid.UUID):
        '''
        获取应用
        :return:
        '''
        app = self.app_service.get_app(id)
        if app is None:
            return fail_message('应用不存在')

        return success_json(app.to_dict())

    def update_app(self,id:uuid.UUID):
        '''
        更新应用
        :return:
        '''
        app = self.app_service.update_app(id)
        if app is None:
            return fail_message('应用不存在')
        return success_message(f"应用更新成功,更新后的名称为：{app.name}")

    def delete_app(self,id:uuid.UUID):
        '''
        删除应用
        :return:
        '''
        app = self.app_service.delete_app(id)
        if app is None:
            return fail_message('应用不存在')
        elif not isinstance(app,App):
            return fail_message('应用删除失败')
        return success_message(f"应用删除成功,id为：{app.id}")
    def completion(self):
        '''
        completion
        :return:
        '''

        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)

        # 1.提取从接口中获取的输入,POST
        query = request.json.get('query')
        # 2.构建0penAI客户端，
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "你是一个OPENAI的开发聊天机器人."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
        )
        # #3.得到请求响应，然后将0penAI的响应传递给前端
        content = completion.choices[0].message.content
        return success_json({'content':content})

    def langchain_completion(self,id:uuid.UUID):
        '''
        langchain completion
        :return:
        '''
        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)

        # 1.提取从接口中获取的输入,POST
        query = request.json.get('query')

        # 2.构建llm客户端，
        llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

        # 3.构建提示词
        prompt = ChatPromptTemplate.from_template(f"请根据用户的提问进行回复.\n{query}")

        # 4.构建解析器
        parser = StrOutputParser()

        # 5.调用
        # content = parser.invoke(llm.invoke(prompt.invoke({"query": query})))

        #改成链式调用
        content = (prompt | llm | parser).invoke({"query": query})

        return success_json({'content':content})


    def ping(self):
        '''
        ping
        :return:
        '''
        # 手动抛出异常错误
        raise FailException(message='错误：ping 接口报错')
        return success_json(data={'ping':'pong'})