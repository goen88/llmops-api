from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from injector import Binder, Module
from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate


# 定义injector扩展module
class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)  # 注入SQLAlchemy
        binder.bind(Migrate, to=migrate) # 注入Migrate
