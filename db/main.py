from sqlalchemy.ext.asyncio import create_async_engine

from core.application import Application
from library.db import DB


async def connect_db(app: Application, loop):
    engine = create_async_engine(
        app.app_settings.DATABASE_STRING, echo=app.app_settings.DEBUG
    )
    db = DB(engine)
    await db.connect()
    app.database = db


async def close_db(app: Application, loop):
    await app.database.close()
