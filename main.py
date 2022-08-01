# import asyncio
#
# import orm
# import aiomysql
# from models import User
#
# async def test(loop):
#
#     # await orm.create_pool(user='root', password='123', db='awesome', loop=loop)
#     #
#     # u = User(name='Test', email='test@example.com', passwd='1234567890', image='abut:blank')
#     #
#     # await u.save()
#     loop = asyncio.get_event_loop()
#
#     loop.run_until_complete(test(loop))
#     x = aiomysql.create_pool(
#
#         user='root',
#         password='123',
#         db='mysql',
#         charset='utf8',
#         autocommit=True,
#         maxsize=10,
#         minsize=1,
#         loop=loop
#     )
#     print(x)
#
#

import orm
from models import User, Blog, Comment
import asyncio


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()



loop = asyncio.get_event_loop()

loop.run_until_complete(test(loop))
for x in test(loop=loop):
    pass
