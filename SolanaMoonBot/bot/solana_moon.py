"""
"""

from bot.interface import keyboard
from logger import get_bot_logger

from aiogram import Bot, methods
from aiogram.utils.token import TokenValidationError


class SolanaMoon:
    def __init__(self, token, *args, **kwargs):
        """
        """
        
        self.bot = Bot(token)
        self.logger = get_bot_logger()
        
    async def setup_bot(self):
        await self.bot.set_my_description("Trade memcoin on solana")
        
    
    async def run_bot(self):
        """
        """
        await self.setup_bot()
        while True:
            pass