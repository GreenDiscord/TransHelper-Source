# Discord Imports
import discord
from discord.ext import commands

# Other Imports
import random


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.db = bot.db
        self.START_BAL = 250

    @commands.command()
    async def shop(self, ctx):
        e = discord.Embed(title="**Shop**",
                          description="Items In The Shop Today:")
        e.add_field(
            name="**You**", value=f"The price of **You** is 1000000, this changes everyday.")
        e.add_field(
            name="**Bear**", value=f"The price of **Bear** is 10000, this changes everyday.")
        await ctx.send(embed=e)

    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        tewq = "They"
        if member is None:
            member = ctx.message.author
            tewq = "You"

        cursor = await self.bot.db.cursor()
        res = cursor.fetchone()
        FIRSTITEM = "ITEMMM"
        USER_ID = member.id
        USER_NAME = str(member)

        await cursor.execute(f"SELECT user_id FROM mail WHERE user_id={USER_ID}")
        result_userID = await cursor.fetchone()

        await cursor.execute(f"SELECT balance FROM mail WHERE user_id={USER_ID}")
        result_userBal = await cursor.fetchone()

        if result_userBal[0] < 0:
            e2 = discord.Embed(
                title=f"**{USER_NAME}'s Balance**", description=f"{tewq} have got 0")
            await ctx.send(embed=e2)
        else:
            e = discord.Embed(title=f"**{USER_NAME}'s Balance**",
                              description=f"{tewq} have got {result_userBal[0]}")
            await ctx.send(embed=e)

    @commands.command()
    @commands.is_owner()
    async def add_money(self, ctx, ammount, member: discord.Member = None):
        if member is None:
            member = ctx.message.author

        cursor = await self.bot.db.cursor()
        USER_ID = member.id
        USER_NAME = str(member)

        await cursor.execute("UPDATE mail SET balance = balance + ? WHERE user_id=?", (ammount, USER_ID))
        await self.bot.db.commit()
        e = discord.Embed(title="Added Money",
                          description=f"Added {ammount} into {member} account!")
        await ctx.reply(embed=e)

    @commands.command()
    @commands.is_owner()
    async def remove_money(self, ctx, ammount, member: discord.Member = None):
        if member is None:
            member = ctx.message.author

        cursor = await self.bot.db.cursor()
        USER_ID = member.id
        USER_NAME = str(member)

        await cursor.execute("UPDATE mail SET balance = balance - ? WHERE user_id=?", (ammount, USER_ID))
        await self.bot.db.commit()
        e = discord.Embed(
            title="Removed Money", description=f"Removed {ammount} out of {member}'s account!")
        await ctx.reply(embed=e)

    @commands.command()
    async def buy(self, ctx, item):
        cursor = await self.bot.db.cursor()
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)
        list1 = ["bear", "you"]
        item = f"{item}"

        if item in list1:
            prices = dict([("bear", 10000), ("you", 1000000)])
            if item in prices:
                itemprice = (prices[item])
                await cursor.execute(f"SELECT balance FROM mail WHERE user_id={USER_ID}")
                result_userBal = await cursor.fetchone()

                if result_userBal[0] < itemprice:
                    e3 = discord.Embed(title="**Purchase Error Has Happened**",
                                       description=f"You need {itemprice} to get {item}!")
                    await ctx.send(embed=e3)
                else:
                    await cursor.execute("UPDATE mail SET balance = balance - ? WHERE user_id=?", (itemprice, USER_ID))
                    await self.bot.db.commit()
                    e = discord.Embed(title="**Item Purchased!**",
                                      description=f"You Have Purchased {item}!")
                    await ctx.send(embed=e)
            else:
                e2 = discord.Embed(title="**Item Not Purchased!**",
                                   description=f"You Have Tried To Purchase {item}, But It Doesn't Exsist!")
                await ctx.send(embed=e2)

    @commands.command()
    async def createaccount(self, ctx):
        cursor = await self.bot.db.cursor()
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)
        FIRSTITEM = "choclate"

        await cursor.execute(f"SELECT user_id FROM mail WHERE user_id={USER_ID}")
        result_userId = await cursor.fetchone()

        if result_userId == None:
            await cursor.execute("INSERT INTO mail(user_name, balance, user_id) values(?,?,?)", (USER_NAME, self.START_BAL, USER_ID))
            await self.bot.db.commit()
            e = discord.Embed(title=f"**Account Created**",
                              description=f"I have made a account for you {ctx.message.author.mention}")
            await ctx.send(embed=e)

        else:
            lis = ["Stan Lee", "Cat", "Trans Leader", "MrBeast", "Girl In Red"]
            e2 = discord.Embed(title="**You already have a account!**",
                               description=f"You already own an account {ctx.author.mention},    'You're not getting any more money from me - {random.choice(lis)}'")
            await ctx.send(embed=e2)

    @commands.command()
    async def beg(self, ctx):
        cursor = await self.bot.db.cursor()
        USER_ID = ctx.message.author.id
        USER_NAME = str(ctx.message.author)
        FIRSTITEM = "CHOCLATE"
        addup = random.randint(0, 1000)
        await cursor.execute("UPDATE mai SET balance = balance + ? WHERE user_id=?", (addup, USER_ID))
        await self.bot.db.commit()
        lis = ["Stan Lee", "Cat", "Trans Leader", "MrBeast", "Girl In Red"]
        e = discord.Embed(
            title=f"**Beg For {USER_NAME}**", description=f"You have gotten `£{addup}` from {random.choice(lis)}")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Economy(bot))
