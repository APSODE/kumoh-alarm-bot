from discord.app_commands import CommandTree
from discord.ext.commands import Bot, Context
from discord import Intents, Object
from src.bot.CogManager import CogManager


MY_GUILD = Object(id = 954253927526830121)

class BotCore(Bot):
    def __init__(self):
        intent = Intents.default()
        intent.message_content = True
        super().__init__(
            intents = intent,
            command_prefix = "!",
            application_id = 1488471141160062986,
            tree_cls = CommandTree
        )
        self._cog_manager = CogManager.create_manager(bot_instance = self)
        self._start()

    async def setup_hook(self) -> None:
        await self._setup_command()
        await self.tree_sync()

    async def tree_sync(self) -> None:
        self.tree.copy_global_to(guild = MY_GUILD)
        synced_result = await self.tree.sync(guild = MY_GUILD)
        print("sync success")
        for idx, command in enumerate(synced_result):
            print(f"Command {idx + 1} : {command}")
        self.tree.copy_global_to(guild = MY_GUILD)

    def _start(self):
        self.run()

    async def _setup_command(self):
        await self._cog_manager.setup_cogs()

        @self.command(name = "prefix_clear")
        async def prefix_clear(ctx: Context):
            await ctx.send("prefix clear command start")
            self.tree.clear_commands(guild = MY_GUILD)
            await ctx.send("prefix clear command end")

        @self.command(name = "prefix_sync")
        async def prefix_sync(ctx: Context):
            await ctx.send("prefix sync command start")
            await self.tree_sync()
            await ctx.send("prefix sync command end")
