from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Executable


async def get_result_all(session: AsyncSession, statement: Executable) -> list:
    pre_res = await session.execute(statement)
    results = pre_res.scalars().all()
    return results
