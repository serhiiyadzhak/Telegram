import asyncio
import logging
from config import *
from rss_feed_handler import get_rss_feed_posts
from send_to_telegram import send_to_telegram


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)


async def periodic_task():
    while True:
        for i in feed_urls:
            posts = await get_rss_feed_posts(i)
            if posts:  
                await send_to_telegram(posts)
        await asyncio.sleep(60) 


async def main():
    task = asyncio.create_task(periodic_task())
    await task


if __name__ == '__main__':
    asyncio.run(main())