from pydantic import BaseModel, Field


class SanicConfig(BaseModel):
    SANIC_HOST: str = Field('0.0.0.0', env='SANIC_HOST')
    SANIC_PORT: int = Field(8000, env='SANIC_PORT')
    SANIC_WORKERS_COUNT: int = Field(1, env='SANIC_WORKERS_COUNT')
