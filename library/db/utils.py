from typing import Optional

from sqlalchemy.engine import CursorResult, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Executable

from db.models.base import DBModel


async def _get_scalar_result(session: AsyncSession, statement: Executable) -> ScalarResult:
    cur_result: CursorResult = await session.execute(statement)
    return cur_result.scalars()


async def get_result_all(session: AsyncSession, statement: Executable) -> list:
    scalars = await _get_scalar_result(session, statement)
    results = scalars.all()

    return results


async def get_result_first(session: AsyncSession, statement: Executable) -> Optional[DBModel]:
    scalars = await _get_scalar_result(session, statement)
    result = scalars.first()

    return result


async def get_result_exact_one(session: AsyncSession, statement: Executable) -> DBModel:
    scalars = await _get_scalar_result(session, statement)
    result = scalars.one()

    return result
