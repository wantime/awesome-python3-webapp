from orm import create_pool
from models import User, Blog, Comment
import asyncio


async def test(loop):
    await create_pool(loop, user='www-data', password='www-data', database='awesome')
    user = User(id=2, name='b', email='b@example', passwd='123', image='about:blank')
    await user.save()


if __name__ == '__main__':


    loop = asyncio.get_event_loop()


    loop.run_until_complete(test(loop))



