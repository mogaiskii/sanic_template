from sanic.request import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.users_list import ResponseUsers
from core.application import Application
from db import models
from library.db.utils import get_result_all
from routes.base import Controller


class UsersListController(Controller):

    async def get(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        stmt = select(models.User)
        users = await get_result_all(session, stmt)
        response = ResponseUsers().dump(dict(users=users))
        return self.json_response(response)
