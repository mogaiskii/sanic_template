from sanic.request import Request
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.auth import RequestAuth, ResponseAuth
from core.application import Application
from core.users import UsersManager
from core.users.exceptions import WrongCredentialsException
from routes.base import Controller


class UserAuthController(Controller):

    async def post(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        request_data = RequestAuth().get_object(request.json)

        manager = UsersManager(session, app.app_settings)
        try:
            user = await manager.get_auth_user(request_data.login, request_data.password)
        except NoResultFound:
            raise WrongCredentialsException

        tokens_pair = manager.create_tokens(user)
        auth = tokens_pair.auth_token
        refresh = tokens_pair.refresh_token

        response = ResponseAuth().dump_from(user=user, tokens=dict(auth_token=auth, refresh_token=refresh))
        return self.json_response(response)
