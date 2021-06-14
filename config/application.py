from pydantic import BaseSettings, Field

from .sanic_config import SanicConfig


class AppConfig(BaseSettings):
    DEBUG: bool = Field(False, env='DEBUG')
    JWT_SECRET: str = Field('s3c$3#_jwT', env='JWT_SECRET')
    DATABASE_STRING: str = Field('postgresql+asyncpg://user:password@0.0.0.0:5432/little-cms', env="DATABASE_STRING")
    PASSWORD_SALT: str = Field('5?nF=K5NWkW.', env='PASSWORD_SALT')

    sanic: SanicConfig = SanicConfig()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
