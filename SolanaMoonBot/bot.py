"""
"""

from logger import get_bot_logger

from aiogram import Bot
from aiogram.utils.token import TokenValidationError
from dotenv import load_dotenv

import os

if __name__ == '__main__':
    load_dotenv()
    logger = get_bot_logger()
    
    try:
        token = os.getenv('TG_BOT_TOKEN_KEY')
    except (TokenValidationError, Exception) as e:
        pass
    
    logger.info(f"Started")