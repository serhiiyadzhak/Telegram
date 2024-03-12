import asyncio
from config import *
from text_processing import *


async def send_to_telegram(posts):
    for post in posts:
        if 'media_type' in post and post['media_type'] == 'video':
            message = f"{translate_text(post['title'], 'uk')}"
            await bot.send_video(chat_id=CHANNEL_NAME, video=post['media_url'], caption=message)
        elif 'media_type' in post and post['media_type'] == 'image':
            message = f"{translate_text(post['title'], 'uk')}"
            await bot.send_photo(chat_id=CHANNEL_NAME, photo=post['media_url'], caption=message)
        else:
            if await is_ukrainian(post['text']):
                message = f"{post['text']}\nRead more: {post['link']}"
            else:
                message = f"{translate_text(post['text'], 'uk')}\nRead more: {post['link']}"
            await bot.send_message(chat_id=CHANNEL_NAME, text=message)
        await asyncio.sleep(30)

