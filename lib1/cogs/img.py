# Discord Imports
import discord
from discord.ext import commands

# Image Imports
from asyncdagpi import ImageFeatures
from PIL import Image, ImageFont, ImageDraw

# Other Imports
from asyncio import sleep
import os



class ImageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.dagpi = bot.dagpi
       
        
    def mycheck():
        def predicate(ctx):
            if ctx.bot.maintenance == True:
                if ctx.author.id == 787800565512929321:
                    return commands.check(predicate)
                else:
                    await ctx.send("Commands are of due to maintance mode!")
                    return False
            else:
                return True
        return commands.check(predicate)

    @commands.group(invoke_without_command=True)
    @mycheck()
    async def img(self, ctx, command=None):
        command2 = self.bot.get_command(f"{command}")
        if command2 is None:
            await ctx.send_help(ctx.command)
        else:
            if command is None:
                await ctx.send_help(ctx.command)
            else:
                pass

    @img.command()
    @mycheck()
    async def wni(self, ctx, *, name):
        text = f"{name} was not the imposter"
        img = Image.open("amongus.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Arial.ttf", 24)
        draw.text((400, 300), text, font=font, fill="white", align="center")
        img.save("wni.png")
        await ctx.send(file=discord.File("wni.png"))
        await sleep(3)
        os.remove("wni.png")

    @img.command()
    @mycheck()
    async def wi(self, ctx, *, name):
        text = f"{name} was the imposter"
        img = Image.open("amongus.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Arial.ttf", 24)
        draw.text((400, 300), text, font=font, fill="white", align="center")
        img.save("wi.png")
        await ctx.send(file=discord.File("wi.png"))
        await sleep(3)
        os.remove("wi.png")

    @img.command()
    @mycheck()
    async def triggered(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.triggered(), url)
        e2file = discord.File(fp=img.image, filename=f"triggered.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is triggered!")
        e.set_image(url=f"attachment://triggered.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command(cooldown_after_parsing=True)
    @mycheck()
    async def message(self, ctx, member: discord.Member = None, *, text):
        if member is None:
            member = ctx.author

        uname = member.display_name
        text = str(text)
        pfp = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.discord(),
                                                 url=pfp,
                                                 username=uname,
                                                 text=text)
        e2file = discord.File(fp=img.image, filename=f"message.{img.format}")
        e = discord.Embed(title="Here You Go! Message Sent!")
        e.set_image(url=f"attachment://message.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command(cooldown_after_parsing=True)
    @mycheck()
    async def captcha(self, ctx, member: discord.Member = None, *, text):
        if member is None:
            member = ctx.author

        text = str(text)
        textaslen = len(text)
        if textaslen > 13:
            await ctx.send("Maybe something smaller then 13?")
        else:
            pfp = str(member.avatar_url_as(format="png", size=1024))
            img = await self.bot.dagpi.image_process(ImageFeatures.captcha(),
                                                     url=pfp,
                                                     text=text)
            e2file = discord.File(
                fp=img.image, filename=f"captcha.{img.format}")
            e = discord.Embed(title="Here You Go! Another Captcha?")
            e.set_image(url=f"attachment://captcha.{img.format}")
            await ctx.send(file=e2file, embed=e)

    @img.command()
    @mycheck()
    async def pixel(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.pixel(), url)
        e2file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is pixel!")
        e.set_image(url=f"attachment://pixel.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command()
    @mycheck()
    async def jail(self, ctx, member: discord.Member = None):
        """Yes."""
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.jail(), url=url)
        e2file = discord.File(fp=img.image, filename=f"jail.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is jail!")
        e.set_image(url=f"attachment://jail.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command()
    @mycheck()
    async def magik(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.magik(), url)
        e2file = discord.File(fp=img.image, filename=f"magik.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is magik!")
        e.set_image(url=f"attachment://magik.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command()
    @mycheck()
    async def wanted(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.wanted(), url)
        e2file = discord.File(fp=img.image, filename=f"wanted.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is wanted!")
        e.set_image(url=f"attachment://wanted.{img.format}")
        await ctx.send(file=e2file, embed=e)

    @img.command()
    @mycheck()
    async def rainbow(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.gay(), url)
        e2file = discord.File(fp=img.image, filename=f"rainbow.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is gay!")
        e.set_image(url=f"attachment://rainbow.{img.format}")
        await ctx.send(embed=e, file=e2file)

    @img.command()
    @mycheck()
    async def pan(self, ctx, *, name):
        text = f"Yay! {name} Has come out as pan! :)"
        img = Image.open("pan1.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Arial.ttf", 50)
        draw.text((250, 300), text, font=font, fill="Black", align="center")
        img.save("enby.png")
        await ctx.send(file=discord.File("enby.png"))
        await sleep(3)
        os.remove("enby.png")

    @img.command()
    @mycheck()
    async def enby(self, ctx, *, name):
        text = f"Yay! {name} Has come out as enby!"
        img = Image.open("enby1.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Arial.ttf", 160)
        draw.text((1700, 1100), text, font=font, fill="Black", align="center")
        img.save("enby.png")
        await ctx.send(file=discord.File("enby.png"))
        await sleep(3)
        os.remove("enby.png")

    @img.command()
    @mycheck()
    async def bi(self, ctx, *, name):
        text = f"Yay! {name} Has come out as bisexual! Well done!"
        img = Image.open("bi1.jfif")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Arial.ttf", 14)
        draw.text((30, 90), text, font=font, fill="Black", align="center")
        img.save("bi.png")
        await ctx.send(file=discord.File("bi.png"))
        await sleep(3)
        os.remove("bi.png")


def setup(bot):
    bot.add_cog(ImageManipulation(bot))
