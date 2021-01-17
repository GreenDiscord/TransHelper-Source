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
        self.channel = self.bot.get_channel(800450802174263356)
 
    
    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        logger.info('Attempting to post server count')
        await self.channel.send("Starting to attempt server count update!")
        try:
            await self.dblpy.post_guild_count()
            logger.info('Posted server count ({})'.format(self.dblpy.guild_count()))
            await self.channel.send(f'Updated server count to {len(self.bot.guilds)}')
        except Exception as e:
            logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await self.channel.send('Failed to post server count\n{}: {}'.format(type(e).__name__, e)")
            


        await asyncio.sleep(1800)

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(TopGG(bot))
