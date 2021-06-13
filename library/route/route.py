from sanic import Sanic


class Route:
    def __init__(self, endpoint, path: str, methods: set):
        self.endpoint = endpoint
        self.path = path
        self.methods = methods

    def set_route(self, app: Sanic):
        app.add_route(self.endpoint.as_view(), self.path, methods=self.methods)
