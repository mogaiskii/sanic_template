from goodconf import GoodConf

from .sanic_config import SanicConfig


class AppConfig(GoodConf):
    DEBUG: bool = True
    JWT_SECRET: str = 's3c$3#_jwT'
    DATABASE_STRING: str = 'postgresql+asyncpg://user:password@localhost:5432/little-cms'

    sanic = SanicConfig()
