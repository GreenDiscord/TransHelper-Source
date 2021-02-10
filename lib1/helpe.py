import discord
import asyncio
from discord.ext import commands

class Help(commands.MinimalHelpCommand):
    async def send_pages(self):
        async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases

        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        mess = ctx.message
        mess.add_reaction("👍")
        mes = await channel.send(embed=embed)
        await asyncio.sleep(40)
        await mess.remove_reaction("👍", ctx.guild.me)
        await mes.delete()
            
    
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

        
