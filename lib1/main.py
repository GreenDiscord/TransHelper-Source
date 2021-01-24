import threading
import discord
import json
import os
import async_cleverbot as ac
import cogs
from discord.ext import commands
import os
from datetime import datetime
import aiosqlite
from discord.ext.buttons import Paginator
from helpe import NewHelp
from asyncdagpi import Client
import time
import mystbin

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass




intents = discord.Intents.default()
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

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=NewHelp(),  allowed_mentions=discord.AllowedMentions(users=True, roles=False, everyone=False, replied_user=True), case_insenstive=True)
bot.db = aiosqlite.connect("main.sqlite")
bot.mystbin_client = mystbin.Client()
bot.version = "15"
START_BAL = 250
token = open("toke.txt", "r").read()
bot.load_extension("jishaku")
hce = bot.get_command("help")
hce.hidden = True
dagpitoken = open("asy.txt", "r").read()
topastoken = open("top.txt", "r").read()
chatbottoken = open"chat.txt", "r").read()
bot.topken = f"{topastoken}"
bot.chatbot = ac.Cleverbot(f"{chatbottoken}")
bot.dagpi = Client(dagpitoken)
bot.start_time = time.time()



  

@bot.event
async def on_reaction_add(reaction, member):
    schannel = bot.get_channel(802489970165153812)
    
    if (reaction.emoji == '⭐') and (reaction.count >= 3):
        embed = discord.Embed(color = 15105570)
        embed.set_author(name = reaction.message.author.name, icon_url = reaction.message.author.avatar_url)
        embed.add_field(name = "Message Content", value = f"[{reaction.message.content}]({reaction.message.jump_url})")
        
        if len(reaction.message.attachments) > 0:
            embed.set_image(url = reaction.message.attachments[0].url)
        
        embed.set_footer(text = f" ⭐ {reaction.count} | # {reaction.message.channel.name} | {reaction.message.guild}")
        embed.timestamp = datetime.utcnow()
        await schannel.send(embed = embed)

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
  await cursor.execute("""CREATE TABLE IF NOT EXISTS warns1(num INTEGER NOT NULL PRIMARY KEY, warns INTEGER, user_id INTEGER)""")
  await bot.db.commit()
  bot.description = f"Multi-Purpose Discord.py bot used in {len(bot.guilds)} guilds!"
  print('bot ready')

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        pass
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'prefix' in message.content.lower():
            await  message.channel.send('A full list of all commands is available by typing ```th,help```')
        else:
            pass
    if 'instagram.com' in message.clean_content.lower():
        await message.add_reaction('💩')
    if 'instagram is good' in message.clean_content.lower():
        await message.add_reaction('❌')
    if 'instagram is spyware' in message.clean_content.lower():
        await message.add_reaction('✅')
    await bot.process_commands(message)
    

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
 








@bot.event
async def on_command_error(ctx, error):
  guild = ctx.guild
  member = bot.get_user(787800565512929321)
  if ctx.guild.id == 336642139381301249:
    pass
  if member.id == ctx.author.id:
    pass
  else:
        if isinstance(error, commands.CommandOnCooldown):
            e1 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e1.set_footer(text=f"{ctx.author.name}")
            await ctx.send(embed=e1)
            # await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
            # print("They not patient")
        elif isinstance(error, commands.CommandNotFound):
              e2 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e2.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e2)
              # print(f"again, use help")
              # await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
        elif isinstance(error, commands.MissingPermissions):
              e3 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e3.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e3)
              # await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
              # print(f"your probley dead, so heres the error, {error}")
        elif isinstance(error, commands.MissingRequiredArgument):
              e4 = discord.Embed(title="Command Error!", description=f"`{error}`")
              e4.set_footer(text=f"{ctx.author.name}")
              await ctx.send(embed=e4)
              # await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
              # print(f"Why cant they use help :( {error}")   
        else:
            raise error
            await member.send(f"Guild {guild} has had a error, here it is! `{error}`")
      
      

bot.run(token)
