import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from internal.exception import CustomException
from internal.model import App
from internal.router import Router
from config import Config
from pkg.response import message, fail_message
from pkg.sqlalchemy import SQLAlchemy

class Http(Flask):
    '''
    Http 服务引擎
    '''

    def __init__(
            self,
            *args,
            conf:Config,
            db:SQLAlchemy,
            migrate:Migrate,
            router: Router,
            **kwargs
    ):
        super().__init__(*args, **kwargs)


        # 导入配置文件
        self.config.from_object(conf)

        # 设置自定义异常处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化数据库
        db.init_app(self)
        # 这里修改成migrate方式了
        # with self.app_context():
        #     _ = App()
        #     db.create_all()

        # 初始化数据库迁移
        migrate.init_app(self, db,directory='internal/migration')

        # 解决跨域问题
        #全局解决
        # cors_config = {
        #     "origins": "*",
        #     "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        #     "allow_headers": ["Content-Type", "Authorization"],
        #     "supports_credentials": True  # 添加这个配置
        # }
        # CORS(self, **cors_config)

        CORS(self,resources={
            r'/*':{
                'origins': '*',
                'supports_credentials': True,
                'methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
                'allow_headers': ['Content-Type', 'Authorization'],
            }
        })

        # 注册路由
        router.register_router(self)





    def _register_error_handler(self, error:Exception):
        '''
        注册异常处理
        '''
        # 如果是自定义异常，则提取message和code信息返回
        if isinstance(error, CustomException):
            return message(error.code, error.message)

        # 如果不是自定义异常，则可能内置错误或系统异常，则统一返回Fail消息
        if self.debug or os.getenv('FLASK_ENV')=='development':
            raise error
        else:
            return fail_message(str(error))