import discord
import asyncio
from discord.ext import commands

class Help(commands.MinimalHelpCommand):
    async def send_pages(self):
        ctx = self.context
        mes = ctx.message
        for page in self.paginator.pages:
            embed = discord.Embed(description=page)
            msg = await ctx.send(embed=embed)
            await mes.add_reaction("👍")
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

        
