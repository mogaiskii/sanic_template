from core.application import Application
from db.main import close_db, connect_db
from routes.routes import set_routes


def main():
    from config import settings
    app = Application(name='main')
    app.app_settings = settings
    app.register_listener(connect_db, 'before_server_start')
    app.register_listener(close_db, 'before_server_stop')
    set_routes(app)
    app.run(
        host=settings.sanic.SANIC_HOST,
        port=settings.sanic.SANIC_PORT,
        debug=settings.DEBUG,
        auto_reload=settings.DEBUG,
        workers=settings.sanic.SANIC_WORKERS_COUNT
    )


if __name__ == '__main__':
    main()
