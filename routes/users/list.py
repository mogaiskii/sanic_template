from sanic.request import Request
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.users_list import ResponseUsers
from core.application import Application
from core.users import UsersManager
from library.auth import require_auth
from routes.base import Controller


class UsersListController(Controller):

    @require_auth
    async def get(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        users = await UsersManager(session, app.app_settings).get_all()
        response = ResponseUsers().dump(dict(users=users))
        return self.json_response(response)
