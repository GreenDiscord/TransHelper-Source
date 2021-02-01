from discord.ext import menus
from asyncio import sleep as sl

class VotingMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        return await channel.send(f'I see you would maybe like to vote {ctx.author.mention}, maybe react with your choice :)')

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_check_mark(self, payload):
        await self.message.edit(content=f"Thanks {self.ctx.author.mention}! Here's the [link](https://top.gg/bot/787820448913686539/vote)")


    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        self.stop()
        await self.message.edit(content="Sorry to see you go!")
        await sl(5)
        await self.message.delete()
