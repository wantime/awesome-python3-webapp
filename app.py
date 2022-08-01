import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# 这里接受request，返回Response
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


# 这里是网页服务的初始化
async def init(loop):
	# 使用web.Application()初始化一个app
    app = web.Application(loop=loop)
	# 对它的‘GET’请求绑定一个处理方法
    app.router.add_route('GET', '/', index)
	# 这里协程的方式创建服务
    srv = await loop.create_server(app, '127.0.0.1', 9000)
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
