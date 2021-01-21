import discord
from discord.ext import commands
import mystbin
import random


class MystbinApi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mystbin_client = mystbin.Client()


        @commands.command()
        async def mystbin(self, ctx, *, text):
            paste = await mystbin_client.post(f"{text}", syntax="python")
            e = discord.Embed("I have created a mystbin link for you!", description=f"[Click Here]({paste.url})")
            await ctx.send(embed=e)

        @commands.command()
        async def getmystbin(self, ctx, id):
            get_paste = await mystbin_client.get(f"https://mystb.in/{id}")
            lis = ["awesome","bad","good"]
            e = discord.Embed(title=f"I have found this, is it {random.choice(lis)}?", description=f"The content is shown here:  [Link]({get_paste.url})")


    

def setup(bot):
    bot.add_cog(MystbinApi(bot))
