from discord.ext import commands
import random
import discord
import psutil
import subprocess as sp
import contextlib
import inspect
import time
import copy
import os
import inspect
import io
import textwrap
import traceback
from contextlib import redirect_stdout

import aiohttp
import collections
import ast

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)



async def copy_context_with(ctx: commands.Context, *, author=None, channel=None, **kwargs):

    alt_message: discord.Message = copy.copy(ctx.message)
    alt_message._update(kwargs)  # pylint: disable=protected-access

    if author is not None:
        alt_message.author = author
    if channel is not None:
        alt_message.channel = channel

    # obtain and return a context of the same type
    return await ctx.bot.get_context(alt_message, cls=type(ctx))


class OwnerOnly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def owners(ctx):
      return ctx.author.id == 787800565512929321

    @commands.command(aliases=['s'])
    @commands.is_owner()
    async def sync(self, ctx):
        """Sync with GitHub and reload all the cogs"""
        embed = discord.Embed(title="Syncing...", description="<a:loading:737722827112972449> Syncing and reloading cogs.")
        msg = await ctx.send(embed=embed)
        await os.system("git pull origin master")
        embed = discord.Embed(title="Synced", description="<a:Animated_Checkmark:726140204045303860> Synced with GitHub and reloaded all the cogs.")
        # Reload Cogs as well
        error_collection = []
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.bot.reload_extension(f"cogs.{name}")
                except Exception as e:
                    return await ctx.send(f"```py\n{e}```")
    @commands.group(invoke_without_command=True)
    @commands.check(owners)
    async def dev(self, ctx):
      await ctx.send("commands for my owner only lol")
    
    @dev.group(name='eval')
    @commands.check(owners)
    async def _eval(self, ctx, *, body):
        """Evaluates python code"""
        env = {
            'ctx': ctx,
            'bot': self.bot,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'source': inspect.getsource
        }

        def cleanup_code(content):
            """Automatically removes code blocks from the code."""
            # remove ```py\n```
            if content.startswith('```') and content.endswith('```'):
                return '\n'.join(content.split('\n')[1:-1])

            # remove `foo`
            return content.strip('` \n')

        env.update(globals())

        body = cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        def paginate(text: str):
            '''Simple generator that paginates text.'''
            last = 0
            pages = []
            for curr in range(0, len(text)):
                if curr % 1980 == 0:
                    pages.append(text[last:curr])
                    last = curr
                    appd_index = curr
            if appd_index != len(text)-1:
                pages.append(text[last:curr])
            return list(filter(lambda a: a != '', pages))
        
        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await ctx.message.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                        
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await ctx.message.add_reaction('\u2705')  # tick
        elif err:
            await ctx.message.add_reaction('\u2049')  # x
        else:
            await ctx.message.add_reaction('\u2705')
      
    @dev.group(invoke_without_command=True, name="as")
    @commands.check(owners)
    async def dev_as(self, ctx: commands.Context, target: discord.User, *, command_string: str):
   
        if ctx.guild:
            target_member = None

            with contextlib.suppress(discord.HTTPException):
                target_member = ctx.guild.get_member(target.id) or await ctx.guild.fetch_member(target.id)

            target = target_member or target

        alt_ctx = await copy_context_with(ctx, author=target, content=ctx.prefix + command_string)

        if alt_ctx.command is None:
            if alt_ctx.invoked_with is None:
                return await ctx.send('This bot has been hard-configured to ignore this user.')
            return await ctx.send(f'Command "{alt_ctx.invoked_with}" is not found')

        return await alt_ctx.command.invoke(alt_ctx)
      
    @dev.group(invoke_without_command=True)
    @commands.check(owners)
    async def chnick(self,ctx,*,name):
      me3 = ctx.guild.me
      await me3.edit(nick=name)
      word1 = "Nickname Changed To"
      await ctx.send(f"{word1} {name}")
    
    
    
    
    @dev.group(invoke_without_command=True)
    @commands.check(owners)
    async def changestat(self, ctx):
      await ctx.send(f"Hi yeah")
      
    @changestat.group(invoke_without_command=True)
    @commands.check(owners)
    async def stream(self, ctx, *, activity='placeholder (owner to lazy lol)'):
      await self.bot.change_presence(activity=discord.Streaming(name=activity, url="http://www.twitch.tv/transhelperdiscordbot"))
      await ctx.send(f'Changed activity to {activity} using Stream status.')
       
        
    @changestat.group(invoke_without_command=True)
    @commands.check(owners)
    async def game(self, ctx, *, activity='placeholder (owner to lazy lol)'):
      await self.bot.change_presence(activity=discord.Game(name=activity))
      await ctx.send(f'Changed activity to {activity} using Game status.')
                                     
    @changestat.group(invoke_without_command=True)
    @commands.check(owners)
    async def watching(self, ctx, *, activity='placeholder (owner to lazy lol)'):
      await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
      await ctx.send(f'Changed activity to {activity} using Watching status.')
                                     
    @changestat.group(invoke_without_command=True)
    @commands.check(owners)
    async def listening(self, ctx, *, activity='placeholder (owner to lazy lol)'):
      await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity))
      await ctx.send(f'Changed activity to {activity} using Listening status.')
    

    
    
    
    
    
    
    
    
    
    
    
    
 
    
  
    
    @dev.group(invoke_without_command=True)
    @commands.check(owners)
    async def stop_bot(self, ctx):
        emoji = '\N{THUMBS UP SIGN}'
        message = ctx.message
        await message.add_reaction(emoji)
        await ctx.bot.logout()

    @dev.group(invoke_without_command=True)
    @commands.check(owners)
    async def send(self, ctx, idd, *, message):
        lis = ["antastic",
               "melodic",
               "quick",
               "massive",
               "super",
               "sophisticated",
               "unruly",
               "legal",
               "elite",
               "ludicrous",
               "questionable",
               "fallacious",
               "ratty",
               "chivalrous",
               "didactic",
               "sticky",
               "amuck",
               "supreme",
               "polite",
               "abnormal",
               "hilarious",
               "vacuous",
               "enchanted",
               "real",
               "shaky",
               "infamous",
               "successful",
               "royal",
               "ablaze",
               "delightful",
               "miscreant",
               "flawless",
               "dynamic",
               "woebegone",
               "oopsided",
               "old",
               "acid",
               "vagabond",
               "level"]
        channel = self.bot.get_channel(int(idd))
        await channel.send(f"{message}")
        await ctx.send(f"Your message {message} was sent!")
        await channel.send(f"random word of this message = {random.choice(lis)}")


def setup(bot):
    bot.add_cog(OwnerOnly(bot))
