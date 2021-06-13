from sanic.request import Request
from sanic.response import text
from sqlalchemy.ext.asyncio import AsyncSession

from core.application import Application
from routes.base import Controller


class IndexController(Controller):

    async def get(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        return text("Hi, Mark!")
