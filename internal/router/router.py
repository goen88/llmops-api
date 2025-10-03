from dataclasses import dataclass

from flask import Flask, Blueprint
from internal.handler import AppHandler
from injector import inject


@inject
@dataclass
class Router:
    '''
    路由
    '''

    app_handler: AppHandler

    def register_router(self, app: Flask):
        '''
        注册路由
        '''
        # 1、创建蓝图(蓝图：就是一组路由)
        bp = Blueprint('llmops', __name__,url_prefix='')

        # 2、添加路由
        bp.add_url_rule('/ping',view_func=self.app_handler.ping)
        bp.add_url_rule('/app/completion',methods=['POST'],view_func=self.app_handler.completion)
        bp.add_url_rule('/app/<uuid:id>/langchain_completion',methods=['POST'],view_func=self.app_handler.langchain_completion)
        bp.add_url_rule('/app/create',methods=['POST'],view_func=self.app_handler.create_app)
        bp.add_url_rule('/app/<uuid:id>',methods=['GET'],view_func=self.app_handler.get_app)
        bp.add_url_rule('/app/<uuid:id>',methods=['POST'],view_func=self.app_handler.update_app)
        bp.add_url_rule('/app/<uuid:id>/delete',methods=['POST'],view_func=self.app_handler.delete_app)

        # 3、注册蓝图
        app.register_blueprint(bp)



