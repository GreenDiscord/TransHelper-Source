import threading
import random
import dashcord
from jishaku import voice
from ffmpeg import audio
import discord
import jishaku
import json
import os
import cogs
import spotify
from discord.ext import commands
from pretty_help import PrettyHelp
from gtts import gTTS
from time import sleep as bedtime
import os
import discord.voice_client
import ffmpeg
from AntiSpam import AntiSpamHandler
import aiosqlite
from discord.ext.buttons import Paginator


class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass




intents = discord.Intents.default()
intents.members = True
description = "hi"





bot = commands.Bot(command_prefix="th,", description=description, intents=intents, help_command=PrettyHelp())
bot.db = aiosqlite.connect("main.sqlite")
bot.version = "15"
START_BAL = 250
bot.load_extension("jishaku")




  



@bot.event
async def on_connect():
    print('bot connected')

@bot.event
async def on_ready():
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
  await bot.db
  cursor = await bot.db.cursor()   
  await cursor.execute("""CREATE TABLE IF NOT EXISTS mail(num INTEGER NOT NULL PRIMARY KEY,     user_name TEXT, balance INTEGER, user_id INTEGER)""")
  await bot.db.commit()
  
  print('bot ready')



@bot.event
async def on_member_join(member : discord.Member):
    feedback = bot.get_channel(794164790368796672)
    role = member.guild.get_role(794135439497101323)
    if member.guild.id == 787825469391241217:
        await member.add_roles(role)
    else:
      await feedback.send(f"Guild {member.guild.name} is trying to use auto-role! Contact {member.guild.owner}")



@bot.event
async def on_message(message:discord.Member):
  if message.author.bot:
      return print("hi")
  else:
    lis = ["fuck", "shit", "bastard", "faggot", "Fuck", "Shit", "Bastard", "Faggot"]
    if message.content in lis:
      await message.delete()
      await message.channel.send(f"{message.author.mention} please stop :)")
    else:
      pass
 
  await bot.process_commands(message)
    
  











@bot.event
async def on_command_error(ctx, error):
  guild = ctx.guild
  member = bot.get_user(787800565512929321)
  if isinstance(error, commands.CommandOnCooldown):
      e1 = discord.Embed(title="Command Error!", description=f"`{error}`")
      e1.set_footer(text=f"{ctx.author.name}")
      await ctx.send(embed=e1)
      await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
      print("They not patient")
  elif isinstance(error, commands.CommandNotFound):
        e2 = discord.Embed(title="Command Error!", description=f"`{error}`")
        e2.set_footer(text=f"{ctx.author.name}")
        await ctx.send(embed=e2)
        print(f"again, use help")
        await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
  elif isinstance(error, commands.MissingPermissions):
        e3 = discord.Embed(title="Command Error!", description=f"`{error}`")
        e3.set_footer(text=f"{ctx.author.name}")
        await ctx.send(embed=e3)
        await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
        print(f"your probley dead, so heres the error, {error}")
  elif isinstance(error, commands.MissingRequiredArgument):
        e4 = discord.Embed(title="Command Error!", description=f"`{error}`")
        e4.set_footer(text=f"{ctx.author.name}")
        await ctx.send(embed=e4)
        await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
        print(f"Why cant they use help :( {error}")   
  else:
      raise error
      await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
      
      

bot.run("TOKEN")
