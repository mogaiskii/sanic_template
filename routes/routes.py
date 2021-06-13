from typing import List

from sanic import Sanic

from library.route import Route
from routes import IndexController
from routes.users import UsersListController


GET = 'GET'
POST = 'POST'


def set_routes(app: Sanic):
    routes: List[Route] = [
        Route(IndexController, '/', {GET}),
        Route(UsersListController, '/users', {GET}),
    ]

    for route in routes:
        route.set_route(app)

    return app
