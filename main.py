import asyncio

import orm

from models import User

async def test(loop):

    await orm.create_pool(user='root', password='password', db='awesome', loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='abut:blank')

    await u.save()

loop = asyncio.get_event_loop()

loop.run_until_complete(test(loop))
