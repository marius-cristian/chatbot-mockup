from aiohttp import web
from src.router.routes import init_routes


def init_app(argv=None) -> web.Application:
    app = web.Application()
    init_routes(app)
    return app


app = init_app()