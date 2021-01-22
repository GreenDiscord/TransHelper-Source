import discord
from discord.ext import commands
import datetime
import random
from datetime import  timedelta
from platform import python_version
from time import time
import platform
import asyncio
from apscheduler.triggers.cron import CronTrigger
import time
from discord import Activity, ActivityType, Embed
from discord import __version__ as discord_version
from PIL import Image
import io
from discord.ext.commands import Cog
from discord.ext.commands import command
from psutil import Process, virtual_memory
from discord.utils import get
import robloxpy
import asyncio
from datetime import timedelta
from platform import python_version
from time import time
import os
import time
from gtts import gTTS
from time import sleep as bedtime
from apscheduler.triggers.cron import CronTrigger
from discord import Activity, ActivityType, Embed
from discord import __version__ as discord_version
from discord.ext.commands import Cog
from discord.ext.commands import command
from psutil import Process, virtual_memory 
import hypixel
import random

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.max_concurrency(1, per=commands.BucketType.channel) 
    @commands.command()
    async def reaction(self, ctx):
        """
        Yum Yum or Yuck Yuck?
        """
        cookies = ["🍪", "❤"]
        lis = ["this mighty","this weak","this amazing"]
        reaction = random.choices(cookies, weights=[0.9, 0.1], k=1)[0]
        embed = discord.Embed(description=f"So, {random.choice(lis)} fighter has challenged people to a game of....Cookie? Okay then get ready!")
        message = await ctx.send(embed=embed)
        await asyncio.sleep(4)
        for i in reversed(range(1, 4)):
            await message.edit(embed=discord.Embed(description=str(i)))
            await asyncio.sleep(1)
        await asyncio.sleep(random.randint(1, 3))
        await message.edit(embed=discord.Embed(description=f"React to the {reaction}!"))
        await message.add_reaction(reaction)
        start = time.perf_counter()
        try:
            _, user = await ctx.bot.wait_for(
                "reaction_add",
                check=lambda _reaction, user: _reaction.message.guild == ctx.guild
                and _reaction.message.channel == ctx.message.channel
                and _reaction.message == message and str(_reaction.emoji) == reaction and user != ctx.bot.user
                and not user.bot,
                timeout=60,)
        except asyncio.TimeoutError:
            return await message.edit(embed=discord.Embed(description="No one ate the cookie..."))
        end = time.perf_counter()
        await message.edit(embed=discord.Embed(description=f"**{user}**  ate the cookie in ```{end - start:.3f}``` seconds!"))
        await user.send(f"Well Done! You completed it in ```{end - start:.3f}``` seconds.")
        
    @command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def feedback(self, ctx, *, feed):
      channel = self.bot.get_channel(794164790368796672)
      e = discord.Embed(title="Sent Feedback!", description=f"Your feedback '{feed}' has been sent!")
      await ctx.send(embed=e)
      e2 = discord.Embed(title=f"Oh no, is it bad or good? ({ctx.author} has sent feedback)", description=f"{feed}")
      await channel.send(embed=e2)
    
    @feedback.error
    async def feedback_handler(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            l = self.bot.get_command("feedback")
            e = discord.Embed(title=f"Cooldown left - {l.get_cooldown_retry_after(ctx) * 10000}", color=discord.colour.Color.from_rgb(231, 84, 128))
            await ctx.send(embed=e)
            
            
    
        
    @command()
    async def remind(self, ctx, time, *, reminder):
      e = discord.Embed(title="I will remind you!", descripition=f"I will you remind you in {time} seconds!")
      await ctx.send(embed=e)
      await asyncio.sleep(int(time))
      e2 = discord.Embed(title=f"Hello {ctx.author}", description=f"I have come to remind you to {reminder}!")
      await ctx.message.reply(embed=e2)
      
    @command(pass_context=True)
    async def ar(self, ctx, *, role1):
      member = ctx.message.author
      role = discord.utils.get(member.guild.roles, name=f"{role1}")
      await member.add_roles(role)
      e = discord.Embed(title="Added Roles", description=f"I have added the roles '{role1}' for you!")
      await ctx.send(embed=e)
    
    @command()
    async def ru(self, ctx, user):
      if robloxpy.DoesNameExist(user) == False:
        await ctx.send(f"Member {user} does not exist")
        pass
      else:
        id1 = robloxpy.NameToID(f'{user}')
        e = discord.Embed(title=f"Stats for {robloxpy.GetName(id1)}", description=f"Are they online? {robloxpy.IsOnline(id1)}", inline=True)
        e.add_field(name=f"Account Age (in days)? {robloxpy.AccountAgeDays(id1)}", value=f"Year Account Was Created? {robloxpy.UserCreationDate(id1,'Year')}", inline=True)
        e.add_field(name=f"RAP? {robloxpy.GetUserRAP(id1)}", value=f"Limited Value? {robloxpy.GetUserLimitedValue(id1)}", inline=False)
        e.set_footer(text=f"Banned User? {robloxpy.IsBanned(id1)}")
        await ctx.send(embed=e)
                
    @command()
    async def sn(self, ctx, *, name):       
        tts = gTTS(text=f"Hi! {name} is really cool!", lang='en')
        tts.save("announce.mp3")
        await ctx.send(file=discord.File("announce.mp3"))
        bedtime(5)
        os.remove("announce.mp3")
   
    @command()
    async def tts(self, ctx, *, text):
        lol = gTTS(text=f"{text}")
        lol.save("tts.mp3")
        await ctx.send(file=discord.File("tts.mp3"))
        bedtime(5)
        os.remove("tts.mp3")

    @commands.command(
        name="stats", description="A usefull command that displays bot statistics."
    )
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(
            title=f"{self.bot.user.name} Stats",
            description="\uFEFF",
            colour=ctx.author.colour,
            timestamp=ctx.message.created_at,
        )

        embed.add_field(name="Bot Version:", value=self.bot.version)
        embed.add_field(name="Python Version:", value=pythonVersion)
        embed.add_field(name="Discord.Py Version", value=dpyVersion)
        embed.add_field(name="Total Guilds:", value=serverCount)
        embed.add_field(name="Total Users:", value=memberCount)
        embed.add_field(name="Bot Developers:", value="<@787800565512929321>")

        embed.set_footer(text=f"{ctx.author} | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def show_color(self, ctx, *, color: discord.Colour):
        '''Enter a color and you will see it!'''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)
        
    @command()
    async def hi(self, ctx):
        await ctx.send("hi.")
        
    @command()
    async def level(self, ctx, name):
      level = hypixel.get_level(name) 
      if level is None:
        e = discord.Embed(title=f"{name}", description=f"Player {name} is not found!, Please make sure to use their **Minecraft** username.")
        await ctx.send(embed=e)
      else:
        e1 = discord.Embed(title=f"Level Of User {name}", description=f"{level}")
        await ctx.send(embed=e1)
          
          
    @command()
    async def gay(self, ctx):
      lis = ["1%", "58%", "32%", "85%", "37%", "48%", "50%"]
      await ctx.send(f"You are {random.choice(lis)} gay")

def setup(bot):
    bot.add_cog(Random(bot))
