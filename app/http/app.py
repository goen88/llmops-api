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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
