from typing import Optional

from sanic import response
from sanic.request import Request
from sanic.views import HTTPMethodView
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from core.application import Application


log = get_logger('Controller')


class Controller(HTTPMethodView):

    def dispatch_request(self, request, *args, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        app : Application = request.app
        session = app.database.create_session()
        log.info(f'Started {type(self)}#{request.method.lower()}')
        return handler(request, app, session, *args, **kwargs)

    @staticmethod
    def json_response(data: dict, code: int=200, headers: Optional[dict]=None):
        res = response.json(data, status=code)

        if headers:
            res.headers.update(headers)

        return res

    async def get(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        pass

    async def post(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        pass

    async def put(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        pass

    async def delete(self, request: Request, app: Application, session: AsyncSession, *args, **kwargs):
        pass
