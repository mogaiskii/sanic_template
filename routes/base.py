from contextvars import ContextVar
from typing import Optional
from uuid import uuid4

from marshmallow import ValidationError
from sanic import response
from sanic.request import Request
from sanic.views import HTTPMethodView
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from core.application import Application
from core.exceptions import ServiceException
from library.auth.exceptions import AuthExpiredException, AuthException, ForbiddenException


log = get_logger('Controller')
_log_code: ContextVar[str] = ContextVar('not_set')


class Controller(HTTPMethodView):

    # wrap into async handler with no interface breaking
    def dispatch_request(self, request, *args, **kwargs):
        return self._handle_request(request, *args, **kwargs)

    async def _handle_request(self, request, *args, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        app : Application = request.app
        session = app.database.create_session()
        _log_code.set(str(uuid4()))

        log.info(f'Started {type(self)}#{request.method.lower()} [{self.get_log_code()}]')

        try:
            resp = await handler(request, app, session, *args, **kwargs)
        except ValidationError as e:
            resp = response.json({'error': e.messages}, status=400)
        except AuthExpiredException:
            resp = response.json({'error': 'Token expired'}, status=401)
        except AuthException:
            resp = response.json({'error': 'Not Authorized'}, status=401)
        except ForbiddenException:
            resp = response.json({'error': 'Forbidden'}, status=403)
        except ServiceException as e:
            resp = e.get_json_response()
        except Exception as e:
            log.error(e,exc_info=1)
            resp = ServiceException(e).get_json_response()

        await session.close()
        log.info(f'Finished {type(self)}#{request.method.lower()} [{self.get_log_code()}]')

        return resp

    @staticmethod
    def get_log_code():
        return _log_code.get()

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
