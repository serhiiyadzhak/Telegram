from telegram import Bot
from transformers import pipeline
import os


MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHANNEL_NAME = os.environ.get("CHANNEL_NAME")


summarizer = pipeline("summarization")
bot = Bot(token=TELEGRAM_TOKEN)


feed_urls = ['https://9gagrss.com/feed/',
             'https://www.atlanticcouncil.org/issue/conflict/feed/',
             'https://www.ft.com/war-in-ukraine?format=rss',
             'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/news-event/ukraine-russia/rss.xml',
             'https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best',
             'https://www.pravda.com.ua/rss/', 
             'http://feeds.bbci.co.uk/news/rss.xml', 
             'http://rss.cnn.com/rss/edition.rss', 
             'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
             'https://www.ft.com/rss/home/uk']
