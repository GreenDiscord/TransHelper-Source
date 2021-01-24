import discord, datetime, time, random, asyncio
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.chatbot = bot.chatbot
    
    @commands.max_concurrency(1, per=BucketType.channel, wait=False)
    @commands.command(aliases=['cb'])
    async def chatbot(self, ctx):
        '''Talk to chatbot'''
        lis = ["cancel", "end", "im bored now bye"]
        transmit = True
        await ctx.send(f'Chatbot Started!\nType the following items `{lis}` to end.')
        while transmit is True:
            try:
                m = await self.bot.wait_for('message', timeout=30, check=lambda m:(ctx.author == m.author and ctx.channel == m.channel))
            except asyncio.TimeoutError:
                await ctx.send("I'm bored now, you should of been quicker...")
                transmit = False
            else:
                if m.content.lower() == lis:
                    transmit = False
                    left = await self.bot.chatbot.ask("bye")
                    await ctx.send(f"{left.text}... Waiting... OH you said cancel, bye!")
                else:
                    async with ctx.channel.typing():
                        response = await self.bot.chatbot.ask(m.content) 
                        await ctx.send(response.text)
    
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
            if not user.id == 787800565512929321:
               return await ctx.send("Hahaha, Your not wining, only Green can :)")
        except asyncio.TimeoutError:
            return await message.edit(embed=discord.Embed(description="No one ate the cookie..."))
        end = time.perf_counter()
        await message.edit(embed=discord.Embed(description=f"**{user}**  ate the cookie in ```{end - start:.3f}``` seconds!"))
        lis3 = ["1", "2"]
        choice = random.choice(lis3)
        if choice == 2:
             await user.send(f"Firstly, Random chose 2 so you get this DM, Secondly, Well Done! You completed it in ```{end - start:.3f}``` seconds.")
        else:
             pass

    @commands.max_concurrency(1, per=BucketType.guild, wait=False)
    @commands.command(aliases=['2048', '24'])
    async def twenty(self, ctx):
        """Starts a 2048 game inside of Discord (just dm the bot your score)"""
        ## Made by NeuroAssassin [https://github.com/NeuroAssassin/Toxic-Cogs/blob/master/twenty/twenty.py]
        board = [
            ["_", "_", "_", "_"],
            ["_", "_", "_", "_"],
            ["_", "_", "_", "_"],
            ["_", "_", "_", 2],
        ]
        score = 0
        total = 0
        embed=discord.Embed(title="2048", description=f"If a reaction is not received every 2 minutes, the game will time out.\n\n```{self.print_board(board)}```")
        message = await ctx.send(embed=embed)
        await message.add_reaction("\u2B06")
        await message.add_reaction("\u2B07")
        await message.add_reaction("\u2B05")
        await message.add_reaction("\u27A1")
        await message.add_reaction("\u274C")

        def check(reaction, user):
            return (
                (user.id == ctx.author.id)
                and (str(reaction.emoji) in ["\u2B06", "\u2B07", "\u2B05", "\u27A1", "\u274C"])
                and (reaction.message.id == message.id)
            )

        while True:
            try:
                reaction, user = await self.bot.wait_for(
                    "reaction_add", check=check, timeout=120.0
                )
            except asyncio.TimeoutError:
                await ctx.send(f"Ending game.\nYour score was **{score}**")
                await message.delete()
                return
            else:
                try:
                    await message.remove_reaction(str(reaction.emoji), ctx.author)
                except discord.errors.Forbidden:
                    pass
                if str(reaction.emoji) == "\u2B06":
                    msg, nb, total = self.execute_move("up", board)
                elif str(reaction.emoji) == "\u2B07":
                    msg, nb, total = self.execute_move("down", board)
                elif str(reaction.emoji) == "\u2B05":
                    msg, nb, total = self.execute_move("left", board)
                elif str(reaction.emoji) == "\u27A1":
                    msg, nb, total = self.execute_move("right", board)
                elif str(reaction.emoji) == "\u274C":
                    await ctx.send(f"Ending game.\nYour score was **{score}**")
                    await message.delete()
                    return
                score += total
                if msg == "Lost":
                    await ctx.send(
                        f"Oh no!  It appears you have lost {ctx.author.mention}.  You finished with a score of {score}!"
                    )
                    await message.delete()
                    return
                board = nb
                sem=discord.Embed(title=f"Score: **{score}**", description=f"```{self.print_board(board)}```")
                'await message.edit(content=f"Score: **{score}**```{self.print_board(board)}```")'
                await message.edit(embed=sem)


def setup(bot):
    bot.add_cog(Games(bot))
