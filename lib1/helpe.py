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
            await mes.remove_reaction("👍", ctx.guild.me)
            await msg.delete()
    
    def get_command_signature(self, command):
        prefixe = f"{command.name}" 
        prefix = f"{command.aliases}"
        prefixes = f"{command.description}"
        return prefixe + prefix + prefixs
    
    def get_opening_note(self):
        ctx = self.context
        return f"Thank's for using {ctx.guild.me.mention}, the list below shows all commands in their respective groups :)"

    async def command_not_found(self, command):
        destination = self.get_destination()
        embed=discord.Embed(title="Help Error", description=f"Command '{command}' Not Found!")
        await destination.send(embed=embed)
    
    async def subcommand_not_found(self, command):
        destination = self.get_destination()
        embed=discord.Embed(title="Help Error", description=f"Command '{command}' Not Found!")
        await destination.send(embed=embed)

        
