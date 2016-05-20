from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view(hello_world, route_name='home')
    # config.scan()
    return config.make_wsgi_app()
