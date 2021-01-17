from PIL import Image, ImageFont, ImageDraw
import discord
from asyncio import sleep
import os
from discord.ext import commands
from contextlib import suppress
from asyncdagpi import ImageFeatures

member_converter = commands.UserConverter()

class NoMemberFound(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        rest = random.choice(data.notfoundelist)
        return f"{rest}\n\nThe Member {self.arg} was not found"

class BetterMemberConverter(commands.Converter):
    async def convert(self, ctx, argument):
        with suppress(Exception):
            mem = await member_converter.convert(ctx, argument)
            return mem
        with suppress(discord.HTTPException):
            mem = await ctx.bot.fetch_user(argument)
            return mem
        raise NoMemberFound(str(argument))



class ImageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.dagpi = bot.dagpi

    @commands.command()
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

    @commands.command()
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
    
    @commands.command()
    async def triggered(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.triggered(), url)
        e2file = discord.File(fp=img.image,filename=f"triggered.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is triggered!")
        e.set_image(url=f"attachment://triggered.{img.format}")
        await ctx.send(file=e2file, embed=e)
    
    @commands.command(cooldown_after_parsing=True)
    async def tweet(self, ctx, member: BetterMemberConverter=None, *, text):
        if member is None:
            member = ctx.author
            
        uname = member.display_name
        text = str(text)
        pfp = str(member.avatar_url_as(format="png", size=1024))
        img = await self.client.dagpi.image_process(ImageFeatures.tweet(),
                                                    url=pfp,
                                                    username=uname,
                                                    text=text)
        e2file = discord.File(fp=img.image, filename=f"tweet.{img.format}")
        e = discord.Embed(title="Here You Go! Tweet Posted!")
        e.set_image(url=f"attachment://tweet.{img.format}")
        await ctx.send(file=e2file, embed=e)
    
    @commands.command()
    async def pixel(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.pixel(), url)
        e2file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is pixel!")
        e.set_image(url=f"attachment://pixel.{img.format}")
        await ctx.send(file=e2file, embed=e)
    
    @commands.command()
    async def magik(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.magik(), url)
        e2file = discord.File(fp=img.image,filename=f"magik.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is magik!")
        e.set_image(url=f"attachment://magik.{img.format}")
        await ctx.send(file=e2file, embed=e)
    
    @commands.command()
    async def wanted(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.wanted(), url)
        e2file = discord.File(fp=img.image,filename=f"wanted.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is wanted!")
        e.set_image(url=f"attachment://wanted.{img.format}")
        await ctx.send(file=e2file, embed=e)
    
    @commands.command()
    async def rainbow(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.gay(), url)
        e2file = discord.File(fp=img.image,filename=f"rainbow.{img.format}")
        e = discord.Embed(title="Here You Go! Filter used is gay!")
        e.set_image(url=f"attachment://rainbow.{img.format}")
        await ctx.send(embed=e, file=e2file)
        
        
    @commands.command()
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
      
     
    @commands.command()
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

     
    @commands.command()
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

