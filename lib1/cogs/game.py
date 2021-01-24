import discord, datetime, time
from discord.ext import commands



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
        while talk is True:
            try:
                m = await self.bot.wait_for('message', timeout=30, check=lambda m:(ctx.author == m.author and ctx.channel == m.channel))
            except asyncio.TimeoutError:
                await ctx.send("I'm bored now, you should of been quicker...")
                transmit = False
            else:
                if m.content.lower() == lis:
                    transmit = False
                    left = await self.bot.chatbot.ask("bye")
                    await ctx.send(f"{left.text}... Waiting... OH you said cancel, bye!)
                else:
                    async with ctx.channel.typing():
                        response = await self.bot.chatbot.ask(m.content) # Ask a question, returns async_cleverbot.cleverbot.Response
                        await ctx.send(response.text)
    
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
        embed=discord.Embed(title="2048", description=f"If a reaction is not received every 2 minutes, the game will time out.\n\n```{self.print_board(board)}```", color=self.bot.color)
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
                sem=discord.Embed(title=f"Score: **{score}**", description=f"```{self.print_board(board)}```", color=self.bot.color)
                'await message.edit(content=f"Score: **{score}**```{self.print_board(board)}```")'
                await message.edit(embed=sem)


def setup(bot):
    bot.add_cog(Games(bot))
