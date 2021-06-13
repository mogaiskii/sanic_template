from sanic import Sanic
from sqlalchemy.ext.asyncio import AsyncEngine

from config.application import AppConfig
from library.db import DB


class Application(Sanic):
    database: DB
    app_settings: AppConfig
