import discord
from discord.ext import commands

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(description=page)
            await destination.send(embed=embed)



class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=MyNewHelp.send_pages)

    

def setup(bot):
    bot.add_cog(HelpCommand(bot))
