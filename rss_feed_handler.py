import feedparser
from bs4 import BeautifulSoup
from database_manager import add_post_link, is_link_stored
from text_processing import generate_summary
import logging


logger = logging.getLogger(__name__)


def extract_media_url(entry):
    try:
        description_content = entry.description
        soup = BeautifulSoup(description_content, 'html.parser')

        if entry.category == 'video':
            video_tag = soup.find('video')
            if video_tag:
                video_source = video_tag.find('source')
                if video_source and 'src' in video_source.attrs:
                    return video_source['src'], 'video'
                
        elif entry.category == 'static':
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                return img_tag['src'], 'image'
            
    except Exception as e:
            logger.error(f"Error extracting media URL: {e}")
    return None, None

async def get_rss_feed_posts(feed_url):
    feed = feedparser.parse(feed_url)
    posts = []

    for entry in feed.entries[:1]:
        if not is_link_stored(entry.link):
            text = entry.title
                # description = entry.description if hasattr(entry, 'description') else ""
                # text = f"{text}: {description}"
            media_url, media_type = extract_media_url(entry)
            summary = await generate_summary(text)
            if summary:
                try:
                    add_post_link(entry.link, summary)
                    post = {"text": summary, "link": entry.link}
                    if media_url:
                        post["media_url"] = media_url
                        post["media_type"] = media_type
                        post["title"] = entry.title
                    posts.append(post)
                    logger.info(f"Added to DB and list: {entry.link}")
                except Exception as e:
                    logger.error(f"Error adding post to DB: {e}")
    return posts
