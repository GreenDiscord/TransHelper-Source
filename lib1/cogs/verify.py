import discord
from discord.ext import commands
import roblox_py
import asyncio
import json
import random
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'lib1/username.json')

class Verify(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.client = roblox_py.Client()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Verify Cog Ready")
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(manage_nicknames=True)
    async def verify(self,ctx):
        if ctx.guild.me.top_role.position < ctx.author.top_role.position:
            return await ctx.send("Please make sure my role is higher than you ")
        with open(my_file,"r") as f:
            data1 = json.load(f)
        if str(ctx.author.id) in data1.keys():
            await ctx.send("You are already verified\n You can re-verify by `b!reverify` ")
            return
        try:
            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description="Please enter your roblox username")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 25 seconds")

            def check(msg):
                return msg.author == ctx.author

            await ctx.send(embed=embed)
            try:
                username = await self.bot.wait_for('message', check=check, timeout=25)
            except asyncio.TimeoutError:
                return await ctx.send(f"You did'nt answer in time {ctx.author.mention}")
            username = str(username.content)
            sentences1 = [f"glasses or soda and soda and key or vase", "lego or soda and pants or book or bus",
                          "glasses or book or bus or nothing or vase", "book or vase or poo or human or something",
                          "vase bus or nothing or nothing", "sorry or nothing", "thank or bus or bus",
                          "nothing or bus and vase", "bye vase or bus", "bus vase and nothing ",
                          "soda or vase nothing ", "roblox cola bus vase ok", "vase or okay", "soda lemon or buy",
                          "cya", "its okay or nothing","pee poo sodaa ee","human vase or bye"]
            sentences = random.choice(sentences1)
            sentences = sentences.strip()
            sentences = str(sentences)
            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description=f"Paste this in your roblox description\n`{sentences}`\n\nSay `done` when done\n Say `cancel` to cancel")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 300 seconds")
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                return await ctx.send(f"You did'nt answer in time {ctx.author.mention}")

            if message.content == "done" or message.content == "Done":
                NOOB = await self.client.get_user_by_name(username=username)
                if NOOB.description == sentences:
                    await ctx.send("Working Please wait", delete_after=10)
                    await asyncio.sleep(1)
                    with open(my_file,"r") as f:
                        data = json.load(f)
                    data[ctx.author.id] = username
                    with open(my_file, "w") as f:
                        json.dump(data, f, indent=3)
                    try:
                        await ctx.author.edit(nick=username, reason="Verification")
                        await ctx.send(f"{ctx.author.mention},Welcome To `{ctx.message.guild.name}`")
                    except discord.Forbidden as A:
                        await ctx.send(f"Well, this is awkward,\n {A}")

                else:
                    await ctx.send(f"You did'nt changed your description\nPlease Verify once again")
                    return
            elif message.content == "cancel" or message.content == "Cancel":
                return await ctx.send("prompt has been cancelled")
        except roblox_py.PlayerNotFound:
            await ctx.send(f"No player found!\n Please verify once more")
        except roblox_py.RateLimited as fs:
            return await ctx.send(f"{fs}")
        except asyncio.TimeoutError:
            return await ctx.send(f"You did'nt answer in time {ctx.author.mention}")
        except Exception as err:
            await ctx.send(f"`{err}`")

    @commands.command()
    @commands.bot_has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def reverify(self, ctx):
        if ctx.guild.me.top_role.position < ctx.author.top_role.position:
            return await ctx.send("Please make sure my role is higher than you ")
        with open(my_file,"r") as f:
            data1 = json.load(f)
        if str(ctx.author.id) not in data1.keys():
            await ctx.send("You First Need To verify to reverify ")
            return

        try:
            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description="Please enter your roblox username")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 25 seconds")

            def check(msg):
                return msg.author == ctx.author

            await ctx.send(embed=embed)
            try:
                username = await self.bot.wait_for('message', check=check, timeout=25)
            except asyncio.TimeoutError:
                return await ctx.send(f"You did'nt answer in time {ctx.author.mention}")
            username = str(username.content)
            sentences1 = [f"glasses or soda and soda and key or vase", "lego or soda and pants or book or bus",
                          "glasses or book or bus or nothing or vase", "book or vase or poo or human or something",
                          "vase bus or nothing or nothing", "sorry or nothing", "thank or bus or bus",
                          "nothing or bus and vase", "bye vase or bus", "bus vase and nothing ",
                          "soda or vase nothing ", "roblox cola bus vase ok", "vase or okay", "soda lemon or buy",
                          "cya", "its okay or nothing", "pee poo sodaa ee", "human vase or bye"]
            sentences = random.choice(sentences1)
            sentences = sentences.strip()
            sentences = str(sentences)
            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description=f"Paste this in your roblox description\n`{sentences}`\n\nSay `done` when done\n Say `cancel` to cancel")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 300 seconds")
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                return await ctx.send(f"You did'nt answer in time {ctx.author.mention}")

            if message.content == "done" or message.content == "Done":
                NOOB = await self.client.get_user_by_name(username=username)
                if NOOB.description == sentences:
                    await ctx.send("Working Please wait", delete_after=10)
                    await asyncio.sleep(1)
                    with open(my_file, "r") as f:
                        data = json.load(f)
                    data[ctx.author.id] = username
                    with open(my_file, "w") as f:
                        json.dump(data, f, indent=3)
                    try:
                        await ctx.author.edit(nick=username, reason="Verification")
                        await ctx.send(f"{ctx.author.mention},Welcome To `{ctx.message.guild.name}`")
                    except discord.Forbidden as A:
                        await ctx.send(f"Well, this is awkward,\n {A}")
                else:
                    await ctx.send(f"You did'nt changed your description\nPlease Verify once again")
                    return
            elif message.content == "cancel" or message.content == "Cancel":
                return await ctx.send("prompt has been cancelled")
        except roblox_py.PlayerNotFound:
            await ctx.send(f"No player found!\n Please verify once more")
        except roblox_py.RateLimited as fs:
            return await ctx.send(f"{fs}")
        except Exception as err:
            await ctx.send(f"`{err}`")
    @commands.command()
    @commands.guild_only()
    async def whois(self,ctx,user:discord.Member=None):
        if user  == None:
            user = ctx.author
        with open(my_file,"r") as f:
            l = json.load(f)
        if str(user.id) not in l.keys():
            return await ctx.send("Please verify first")
        else:
            noob  = l[str(user.id)]
            await ctx.send(f"{user.name}'s Roblox name is `{noob}`")
            f.close()
def setup(bot):
    bot.add_cog(Verify(bot))
