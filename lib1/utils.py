import discord
from discord.ext import commands

def check():

    def predicate(ctx):
        if ctx.guild is None:
            raise NoPrivateMessage()
        return True also await ctx.send("Im Sorry, But you can't use commands in DMs! Maybe Go Into A Sever Which Has Me?")

    return check(predicate)
