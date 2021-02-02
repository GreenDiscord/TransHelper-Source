from discord.ext import menus
import discord
import traceback
from asyncio import sleep as sl

class VotingMenu(menus.Menu):
    def __init__(self, bot):
        super().__init__(timeout=30.0, clear_reactions_after=True)
        self.bot = bot


    async def send_initial_message(self, ctx, channel):
        e = discord.Embed(title="I see you want vote!", description=f"{ctx.author.mention}, maybe react with your choice :)")
        return await channel.send(embed=e)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_check_mark(self, payload):
        e1 = discord.Embed(title="Thanks!", description=f"Thanks {self.ctx.author.mention}! Here's the [link!](https://top.gg/bot/787820448913686539/vote)")
        await self.message.edit(content="", embed=e1)
        self.stop()

    @menus.button('\N{NEGATIVE SQUARED CROSS MARK}')
    async def on_stop(self, payload):
        e2 = discord.Embed(title="Sorry to see you go!", description="Remember you can always re-run the command :)")
        self.stop()
        await self.message.edit(content="", embed=e2)
        await sl(5)
        await self.message.delete()
        
class WhoMenu(menus.Menu):
    def __init__(self, bot):
        super().__init__(timeout=30.0, clear_reactions_after=True)
        self.bot = bot


    async def send_initial_message(self, ctx, channel):
        e = discord.Embed(title="I see you want to know more!", description=f"{ctx.author.mention}, click the checkmark for the Privacy Policy or the crossmark for just info!")
        return await channel.send(embed=e)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_add(self, payload):
        e1 = discord.Embed(title="Well, Heres The Policy :)", description=f"We store this data for a couple reasons.\n Guild IDs are stored for commands like (prefix command, coming soon), so one servers prefix for that certain guild.\n Member IDs are stored for member specfic things, like th,createaccount thats meant to show the balance of that specific user.", color=discord.Colour.from_hsv(random.random(), 1, 1))
        await self.message.edit(content="", embed=e1)
        self.stop()

    @menus.button('\N{NEGATIVE SQUARED CROSS MARK}')
    async def on_stop(self, payload):
        user = self.bot.get_user(787800565512929321)
        e2 = discord.Embed(title="Hey!", description=f"Hi, I'm {self.bot.user}, I am developed by {user.name}, I have been running since the 10/12/20 :)", color=discord.Colour.from_hsv(random.random(), 1, 1))
        self.stop()
        await self.message.edit(content="", embed=e2)
        await sl(5)
        await self.message.delete()
       
       
