from config import summarizer
from deep_translator import GoogleTranslator
from langdetect import detect
import langdetect
import logging


logger = logging.getLogger(__name__)


def translate_text(text, target_lang='uk'):
    """
    """
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)

async def is_ukrainian(text):
    """"""
    try:
        return detect(text) == 'uk'
    except langdetect.lang_detect_exception.LangDetectException:
        return False

sent_posts_links = [] 

async def generate_summary(text):
    try:
        text = text[:1024]
        if await is_ukrainian(text):
            return text
        else:
            summary = summarizer(text, max_length=130, min_length=25, do_sample=False)
            return summary[0]['summary_text']
    except Exception as e:
        logger.error(f"Error generating summary or detecting language: {e}")
        return None
