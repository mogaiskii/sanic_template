from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from config.application import AppConfig
from db.models.base import DBModel
from library.db.utils import get_result_exact_one, get_result_first, get_result_all


class Manager:
    __model__ = DBModel

    def __init__(self, session: AsyncSession, settings: AppConfig):
        self._session = session
        self._settings = settings

    def _get_statement(self, *filter_statements) -> Select:
        stmt = select(type(self).__model__)
        if filter_statements:
            for filter_ in filter_statements:
                stmt = stmt.where(filter_)

        return stmt

    async def get_exact_one(self, *filter_statements):
        stmt = self._get_statement(*filter_statements)

        return await get_result_exact_one(self._session, stmt)

    async def get_by_id(self, id_: int):
        return await self.get_exact_one(type(self).__model__.id == id_)

    async def get_first(self, *filter_statements):
        stmt = self._get_statement(*filter_statements)

        return await get_result_first(self._session, stmt)

    async def get_all(self, *filter_statements, limit=None):
        stmt = self._get_statement(*filter_statements)

        if limit is not None:
            stmt = stmt.limit(limit)

        return await get_result_all(self._session, stmt)
