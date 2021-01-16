import discord
from discord.ext import commands

def check():
    
    def predicate(ctx):
        if ctx.guild is None:
            raise NoPrivateMessage()
        return True

    return check(predicate)
