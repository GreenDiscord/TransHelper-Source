import discord
import asyncio
from discord.ext import commands

class Help(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        ctx = self.context
        channel = await ctx.bot.get_channel(destination.id)
        for page in self.paginator.pages:
            embed = discord.Embed(description=page)
            msg = await channel.send(embed=embed)
            await asyncio.sleep(33)
            await msg.delete()
    
    async def command_not_found(self, command):
        destination = self.get_destination()
        embed=discord.Embed(title="Help Error", description=f"Command '{command}' Not Found!")
        await destination.send(embed=embed)
    
    async def subcommand_not_found(self, command):
        destination = self.get_destination()
        embed=discord.Embed(title="Help Error", description=f"Command '{command}' Not Found!")
        await destination.send(embed=embed)

        
