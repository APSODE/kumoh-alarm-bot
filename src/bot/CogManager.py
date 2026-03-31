import os
from discord.ext.commands import Bot


class CogManager:
    def __init__(self, bot_instance: Bot):
        self._bot = bot_instance

    @staticmethod
    def create_manager(bot_instance: Bot):
        return CogManager(bot_instance = bot_instance)

    async def setup_cogs(self):
        for cog_file in os.listdir(".\\src\\bot\\cogs\\"):
            if cog_file in ["BaseCommand.py", "__pycache__"]:
                pass
            else:
                await self._bot.load_extension(f"src.python.bot.cogs.{cog_file[:-3]}")
