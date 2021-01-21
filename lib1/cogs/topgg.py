import dbl
import discord
from discord.ext import commands, tasks

import asyncio
import logging


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.bot.topken = bot.topken
        self.dblpy = dbl.DBLClient(self.bot, self.bot.topken)
        self.c = self.bot.get_channel(800450802174263356)
 
    
    async def on_guild_post():
        print("Server count posted successfully")
        await self.c.send(f"Server Count Now Updated!, Current Guilds: {len(self.bot.guilds)}")

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(TopGG(bot))
