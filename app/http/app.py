from flask_migrate import Migrate

from internal.server import Http
from internal.router import Router
from injector import Injector
from config import Config
from pkg.sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from .module import ExtensionModule

_ = load_dotenv(find_dotenv())

injector = Injector([ExtensionModule])

conf = Config()
app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router),
)

# 解决跨域
from flask_cors import CORS

cors_config = {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE","OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True  # 添加这个配置
}
CORS(app, **cors_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
