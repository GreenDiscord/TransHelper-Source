from PIL import Image, ImageFont, ImageDraw
import discord
from asyncio import sleep
import os
from discord.ext import commands
from asyncdagpi import ImageFeatures

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
    async def pixel(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.pixel(), url)
        e2file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
        await ctx.send(file=e2file)
    
    @commands.command()
    async def wanted(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.wanted(), url)
        e2file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
        await ctx.send(file=e2file)
    @commands.command()
    async def rainbow(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            
        url = str(member.avatar_url_as(format="png", size=1024))
        img = await self.bot.dagpi.image_process(ImageFeatures.gay(), url)
        e2file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
        await ctx.send(file=e2file)
        
        
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

