from sqlalchemy import select, literal
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from structlog import get_logger


log = get_logger('DB')


class DB:
    def __init__(self, async_engine: AsyncEngine):
        self._engine = async_engine
        self._sessionmaker = sessionmaker(bind=self._engine, class_=AsyncSession)

    async def connect(self):
        self._engine.connect()
        async with self._engine.begin() as conn:
            result = await conn.execute(select(literal('1')))
            result.fetchall()
        log.info('db connected')

    def create_session(self) -> AsyncSession:
        return self._sessionmaker()

    async def close(self):
        await self._engine.dispose()
        log.info('db closed')
