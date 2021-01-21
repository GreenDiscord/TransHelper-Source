import discord
from discord.ext import commands
import mystbin
import random


class MystbinApi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.mystbin_client = bot.mystbin_client


    @commands.command()
    async def mystbin(self, ctx, *, text):
        paste = await self.bot.mystbin_client.post(f"{text}", syntax="python")
        e = discord.Embed(title="I have created a mystbin link for you!", description=f"[Click Here]({paste.url})")
        await ctx.send(embed=e)

    @commands.command()
    async def getmystbin(self, ctx, id):
        try:
            get_paste = await self.bot.mystbin_client.get(f"https://mystb.in/{id}")
            lis = ["awesome","bad","good"]
            e = discord.Embed(title=f"I have found this, is it {random.choice(lis)}?", description=f"The content is shown here:  [Link]({get_paste.url})")
            await ctx.send(embed=e)
        except BadPasteID:
            return await ctx.send(f"Hmmm.. {id} isn't found, try again?")

    

def setup(bot):
    bot.add_cog(MystbinApi(bot))
