import discord
from discord.ext import commands

async def check(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
         return ctx.send("Im Sorry, But you can't use commands in DMs! Maybe Go Into A Sever Which Has Me?")
