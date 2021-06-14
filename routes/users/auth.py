from sanic.request import Request
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.auth import RequestAuth, ResponseAuth
from core.application import Application
from core.users import UsersManager
from routes.base import Controller


class UserAuthController(Controller):

    async def post(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        request_data = RequestAuth().get_object(request.json)
        user = await UsersManager(session, app.app_settings).get_auth_user(request_data.login, request_data.password)
        tokens = {}
        response = ResponseAuth().dump(dict(user=user, tokens=tokens))
        return self.json_response(response)
