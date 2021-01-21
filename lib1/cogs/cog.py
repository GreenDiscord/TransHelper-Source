import discord
from datetime import date
from io import BytesIO
import time
from discord.ext import commands
import random
import inspect
import os

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def who(self, ctx):
      e = discord.Embed(title=f"Hi, I'm {self.bot.user}", description=f"You can find the privacy policy at [this](https://greendiscord.github.io/TransHelper-Source/resources.html \"privacy policy\") link!", color = discord.Colour.from_hsv(random.random(), 1, 1))
      await ctx.send(embed=e)
        
    @commands.command()
    async def vote(self,ctx):
        e = discord.Embed(title=f"Hi, You can vote for me using the link below!", description=f"[Click Here!](https://top.gg/bot/787820448913686539/vote \"Vote\")", color = discord.Colour.from_hsv(random.random(), 1, 1))
        await ctx.send(embed=e)
        
    @commands.command()
    async def source(self, ctx, *, command: str = None):
        """ Displays source code """
        source_url = 'https://github.com/GreenDiscord/TransHelper-Source'
        branch = 'main'
        e = discord.Embed(title="You didn't provide a command, so here's the source!", description=f"[Source]({source_url})")
        if command is None:
            return await ctx.send(embed=e)

        if command == 'help':
            src = type(self.bot.help_command)
            module = src.__module__
            filename = inspect.getsourcefile(src)
        else:
            obj = self.bot.get_command(command.replace('.', ' '))
            if obj is None:
                return await ctx.send('Could not find command.')

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)
        if not module.startswith('discord'):
            # not a built-in command
            location = os.path.relpath(filename).replace('\\', '/')
        else:
            location = module.replace('.', '/') + '.py'
            source_url = 'https://github.com/Rapptz/discord.py'
            branch = 'master'

        final_url = f'<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>'
        e2 = discord.Embed(title=f"Here's The Source For Command {command}", description=f"[Click Here]({final_url})")
        await ctx.send(embed=e2)

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
      """ Get the avatar of you or someone else """
      user = user or ctx.author
      e = discord.Embed(title=f"Avatar for {user.name}")
      e.set_image(url=user.avatar_url)
      await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx):
      """ Get all roles in current server """
      allroles = ""

      for num, role in enumerate(sorted(ctx.guild.roles, reverse=True), start=1):
          allroles += f"[{str(num).zfill(2)}] {role.id}\t{role.name}\t[ Users: {len(role.members)} ]\r\n"

      data = BytesIO(allroles.encode('utf-8'))
      await ctx.send(content=f"Roles in **{ctx.guild.name}**", file=discord.File(data, filename=f"Roles"))

    @commands.command()
    @commands.guild_only()
    async def joinedat(self, ctx, *, user: discord.Member = None):
      """ Check when a user joined the current server """
      if user is None:
          user = ctx.author

      embed = discord.Embed(title = f'**{user}**', description=f'{user} joined **{ctx.guild.name}** at \n{user.joined_at}')
      embed.set_image(url=user.avatar_url)
      await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def mods(self, ctx):
        """ Check which mods are online on current guild """
        message = ""
        all_status = {
            "online": {"users": [], "emoji": "🟢"},
            "idle": {"users": [], "emoji": "🟡"},
            "dnd": {"users": [], "emoji": "🔴"},
            "offline": {"users": [], "emoji": "⚫"}
        }

        for user in ctx.guild.members:
            idd = 790714521642860556
            if user.roles is discord.utils.get(ctx.guild.roles, id=idd):
                if not user.bot:
                    all_status[str(user.status)]["users"].append(f"**{user}**")

        for g in all_status:
            if all_status[g]["users"]:
                message += f"{all_status[g]['emoji']} {', '.join(all_status[g]['users'])}\n"

        await ctx.send(f"Mods in **{ctx.guild.name}**\n{message}")

    @commands.group()
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            find_bots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=find_bots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)

    @server.command(name="avatar", aliases=["icon"])
    @commands.guild_only()
    async def server_avatar(self, ctx):
        """ Get the current server icon """
        if not ctx.guild.icon:
            return await ctx.send("This server does not have a avatar...")
        await ctx.send(f"Avatar of **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @server.command(name="banner")
    @commands.guild_only()
    async def server_banner(self, ctx):
        """ Get the current banner image """
        if not ctx.guild.banner:
            return await ctx.send("This server does not have a banner...")
        await ctx.send(f"Banner of **{ctx.guild.name}**\n{ctx.guild.banner_url_as(format='png')}")

    @commands.command()
    @commands.guild_only()
    async def user(self, ctx, *, user: discord.Member = None):
        """ Get user information """
        user = user or ctx.author

        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Roles", value=show_roles, inline=False)

        await ctx.send(content=f"ℹ About **{user.id}**", embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
