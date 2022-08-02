import logging;

from coroweb import get
from models import User


logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# 这里接受request，返回Response
@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }



# 这里是网页服务的初始化
async def init(loop):
	# 使用web.Application()初始化一个app
    app = web.Application()
	# 对它的‘GET’请求绑定一个处理方法
    app.router.add_get('/', index)
    #app_runner = web.AppRunner(app)
	# 这里协程的方式创建服务
    # srv = web.run_app(app, host='127.0.0.1', port=9000)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	# 对比wsgiref模块的的创建服务器
	# from wsgiref.simple_server import make_server
	# httpd = make_server('', 8000, index)
	# 写入日志
    logging.info('server started at http://127.0.0.1:9000...')
	# 这里的返回值目前还不清楚有什么用。
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
