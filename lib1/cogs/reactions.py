import discord
from discord.ext import commands
  
from datetime import datetime, timedelta
from random import choice

from discord.ext.commands import Cog



class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.db = bot.db
        self.cur = self.db.cursor()

  
#breaking bot

    

def setup(bot):
    bot.add_cog(Reactions(bot))
