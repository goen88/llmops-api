import uuid
from dataclasses import dataclass

from pkg.sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    '''AI应用服务逻辑'''
    db:SQLAlchemy

    def create_app(self)->App:
        """
        创建应用
        :return:
        """
        with self.db.auto_commit():
            app = App(account_id=uuid.uuid4(), name='测试机器人', description='测试机器人描述',icon='')
            # app.account_id = uuid.uuid4()
            # app.icon = ''
            # app.name = '测试机器人'
            # app.description = '测试机器人描述'

            # 保存到数据库
            self.db.session.add(app)
        return app

    def get_app(self,id:uuid.UUID) -> any:
        """
        获取应用
        :param id:
        :return:
        """
        app = self.db.session.query(App).get(id)
        if app:
            return app
        return None

    def update_app(self,id:uuid.UUID)->any:
        with self.db.auto_commit():
            app = self.get_app(id)
            if app:
                app.name = '更新测试机器人'
                return app
        return None

    def delete_app(self,id:uuid.UUID)->any:
        with self.db.auto_commit():
            app = self.get_app(id)
            if app:
                self.db.session.delete(app)
                return app
        return None
