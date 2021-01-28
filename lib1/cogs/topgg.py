import dbl
import discord
from discord.ext import commands


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.bot.topken = bot.topken
        self.dblpy = dbl.DBLClient(self.bot, self.bot.topken, autopost=True) 
        self.c = self.bot.get_channel(800450802174263356)

    async def on_guild_post(self):
        print("Server count posted successfully")
        await self.c.send(f"Updated Top.gg Server Stats, Current Guild Count {len(self.bot.guilds)}")

def setup(bot):
    bot.add_cog(TopGG(bot))
