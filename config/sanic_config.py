from goodconf import GoodConf


class SanicConfig(GoodConf):
    SANIC_HOST: str = '0.0.0.0'
    SANIC_PORT: int = 8000
