import logging
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from config import MONGO_URI, MONGO_DB_NAME


client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]  
posts_collection = db.posts
logger = logging.getLogger(__name__)


def add_post_link(link, summary):
    try:
        posts_collection.insert_one({"link": link, "summary": summary})
        logger.info("Link added to the database.")
    except DuplicateKeyError:
        logger.error("Add link error: Link already exists in the database.")
    
def is_link_stored(link):
    return posts_collection.find_one({"link": link}) is not None
