import logging, os, json, time
from models import User
from aiohttp import web

from jinja2 import Environment, FileSystemLoader

logging.basicConfig(level=logging.INFO)

from coroweb import add_routes, add_static
import orm


from orm import create_pool

def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        return (await handler(request))
    return logger



async def index_test(request):
    res = await User.findAll()
    # users = await User.findAll()
    # print(users)
    s = ''
    for r in res:
        print(type(r))
        s = s + str(r['name']) + '\n'

    return web.Response(text=s)


# 这里是网页服务的初始化
async def init(loop=None):
    app = web.Application()
    # 对它的‘GET’请求绑定一个处理方法
    # 也就是绑定路由
    app.router.add_get('/', index_test)
    await create_pool(loop=None, user='www-data', password='www-data', database='awesome')
    # 写入日志
    logging.info('server started at http://127.0.0.1:9000...')
    # web.run_app(app, host='127.0.0.1', port=9000)
    return app


async def init_db():
    await create_pool(loop=None, user='www-data', password='www-data', database='awesome')


if __name__ == '__main__':
    web.run_app(init(), host='127.0.0.1', port=9000)
