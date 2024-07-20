"""
"""

from logger import get_bot_logger
from bot.solana_moon import SolanaMoon

from dotenv import load_dotenv

import os
import asyncio
import traceback
    

if __name__ == '__main__':
    load_dotenv()
    logger = get_bot_logger()
    
    try:
        token = os.getenv('TG_BOT_TOKEN_KEY')
        
        solana_moon_bot = SolanaMoon(token)
        # await solana_moon_bot.setup_bot()
        asyncio.run(solana_moon_bot.run_bot())
        
    except Exception:
        print(traceback.format_exc())
    
    logger.info("Runing interrupted")