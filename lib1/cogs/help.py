# Discord Imports
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def mycheck():
        def predicate(ctx):
            if ctx.bot.maintenance == True:
                if ctx.author.id == 787800565512929321:
                    return commands.check(predicate)
                else:
                    await ctx.send("Commands are of due to maintance mode!")
                    return False
            else:
                return True
        return commands.check(predicate)

    @commands.command()
    @mycheck()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def support(self, ctx):
        channel = ctx.channel
        chan = self.bot.get_channel(787825469391241220)
        if channel.guild is chan.guild:
            per = ctx.author.mention
            await chan.send(f"{per} in {channel} needs support!")
            await ctx.send(f"General has been notifed!")
        else:
            pass


def setup(bot):
    bot.add_cog(Help(bot))
