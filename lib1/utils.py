from discord.ext import menus
import discord
from asyncio import sleep as sl

class VotingMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        e = discord.Embed(title="I see you want vote!", description=f"{ctx.author.mention}, maybe react with your choice :)")
        return await channel.send(embed=e)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_check_mark(self, payload):
        e1 = discord.Embed(title="Thanks!", description=f"Thanks {self.ctx.author.mention}! Here's the [link](https://top.gg/bot/787820448913686539/vote)")
        await self.message.edit(content="", embed=e1)
        await self.stop()

    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        e2 = discord.Embed(title="Sorry to see you go!", description="Remember you can always re-run the command :)")
        self.stop()
        await self.message.edit(content="", embed=e2)
        await sl(5)
        await self.message.delete()
