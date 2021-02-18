import threading
import discord
import json
import os
import async_cleverbot as ac
import cogs
from discord.ext import commands
import os
import aiozaneapi
import asyncio
from datetime import datetime
import aiosqlite
from discord.ext.buttons import Paginator
from helpe import Help
from asyncdagpi import Client
import time
import mystbin

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass




intents = discord.Intents.all()
intents.members = True
intents.reactions = True
intents.guilds = True



async def get_prefix(bot, message):
    if message.guild is None:
        prefixes = ["th,", "th.", "th ", "please dont find this one, "]
    elif message.author.id == 787800565512929321:
        prefixes = ["th,", "th.", "th ", ""]
    else:
        prefixes = ["th,", "th.", "th ", "please dont find this one,"]

    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=Help(),  allowed_mentions=discord.AllowedMentions(users=True, roles=False, everyone=False, replied_user=True),case_insensitive=True)
bot.db = aiosqlite.connect("main.sqlite")
bot.mystbin_client = mystbin.Client()
bot.version = "15"
START_BAL = 250
token = open("toke.txt", "r").read()
bot.load_extension("jishaku")
hce = bot.get_command("help")
hce.hidden = True
dagpitoken = open("asy.txt", "r").read()
robloxcookie = open("roblox.txt", "r").read()
topastoken = open("top.txt", "r").read()
chatbottoken = open("chat.txt", "r").read()
hypixel = open("hypixel.txt", "r").read()
bot.robloxc = f"{robloxcookie}"
bot.hypixel = f"{hypixel}"
bot.topken = f"{topastoken}"
bot.chatbot = ac.Cleverbot(f"{chatbottoken}")
bot.se = aiozaneapi.Client(f'{open("zane.txt", "r").read()}')
bot.dagpi = Client(dagpitoken)
bot.start_time = time.time()
bot.thresholds = (10, 25, 50, 100)
bot.maintenance = False




  



@bot.event
async def on_connect():
    print('bot connected')

@bot.event
async def on_ready():
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
  await bot.db
  current_time = time.time()
  difference = int(round(current_time - bot.start_time))
  bot.stats = bot.get_channel(804496786038980618)
  cursor = await bot.db.cursor()   
  await cursor.execute("""CREATE TABLE IF NOT EXISTS mail(num INTEGER NOT NULL PRIMARY KEY,     user_name TEXT, balance INTEGER, user_id INTEGER)""")
  await bot.db.commit()
  await cursor.execute("""CREATE TABLE IF NOT EXISTS warns1(num INTEGER NOT NULL PRIMARY KEY, warns INTEGER, user_id INTEGER)""")
  await bot.db.commit()
  bot.description = f"Multi-Purpose Discord.py bot used in {len(bot.guilds)} guilds!"
  print(f'Bot ready, running on {discord.__version__} and connected to {len(bot.guilds)}')
  e = discord.Embed(title=f"Bot Loaded!", description=f"Bot ready, loaded all cogs perfectly! Time to load is {difference} secs :)")
  await bot.stats.send(embed=e)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'prefix' in message.content.lower():
            await  message.channel.send('A full list of all commands is available by typing ```th,help```')
    await bot.process_commands(message)

    
@bot.listen()
async def on_invite_update(member, invite):
    await bot.wait_for_invites()
    print(f"{member} joined {member.guild} with invite {invite}")
    can_send = member.guild.system_channel is not None

    if invite.uses in bot.thresholds and can_send:
        try:
            # I am sorry that rocky-wocks was all that came to mind
            await member.guild.system_channel.send(
                f"**Congratulations** to {invite.inviter} for reaching the "
                f"**{invite.uses}** invite threshold! They will be "
                f"rewarded with **{1000*invite.uses:,}** shiny rocky-wocks!"
            )
        except discord.Forbidden:
            print(f"[FAILED] {invite.code} @ {invite.uses} by "
                  f"{invite.inviter}")

@bot.event
async def on_member_join(member : discord.Member):
    feedback = bot.get_channel(794164790368796672)
    role = member.guild.get_role(794135439497101323)
    if member.guild.id == 787825469391241217:
        await member.add_roles(role)
    else:
        pass


    
  

@bot.event
async def on_guild_join(guild):
    await guild.system_channel.send(f'Hey there! do th,help or <@787820448913686539> help for commands!')
 
@bot.command()
async def prefix(ctx):
    pass







@bot.event
async def on_command_error(ctx, error):
  guild = ctx.guild
  if ctx.guild.id == 336642139381301249:
    pass
  if 787800565512929321 == ctx.author.id:
    pass
  else:
        if isinstance(error, commands.CommandOnCooldown):
            e1 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e1.set_footer(text=f"{ctx.author.name}")
            await ctx.send(embed=e1)
        elif isinstance(error, commands.CommandNotFound):
              e2 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e2.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e2)
        elif isinstance(error, commands.MissingPermissions):
              e3 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e3.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e3)
        elif isinstance(error, commands.MissingRequiredArgument):
              e4 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e4.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e4)
        elif isinstance(error, commands.CommandInvokeError):
            haha = ctx.author.avatar_url
            e7 = discord.Embed(title="Oh no green you fucked up", description=f"`{error}`")
            e7.add_field(name="Command Caused By?", value=f"{ctx.command}")
            e7.add_field(name="By?", value=f"ID : {ctx.author.id}, Name : {ctx.author.name}")
            e7.set_thumbnail(url=f"{haha}")
            e7.set_footer(text=f"{ctx.author.name}")
            await ctx.send("New Error, Sending to devs straight away!")
            await bot.stats.send(embed=e7)
        else:
            haaha = ctx.author.avatar_url
            e9 = discord.Embed(title="Oh no green you fucked up", description=f"`{error}`")
            e9.add_field(name="Command Caused By?", value=f"{ctx.command}")
            e9.add_field(name="By?", value=f"ID : {ctx.author.id}, Name : {ctx.author.name}")
            e9.set_thumbnail(url=f"{haaha}")
            e9.set_footer(text=f"{ctx.author.name}")
            await ctx.send("New Error, Sending to devs straight away!")
            await bot.stats.send(embed=e9)
            
      
@bot.event
async def on_command(ctx):
    if bot.maintenance is True:
        return await ctx.send("Maintenance Mode Is On")
    else:
        await ctx.invoke(ctx.command)

bot.run(token)
