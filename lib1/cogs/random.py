        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def show_color(self, ctx, *, color: discord.Colour):
        '''Enter a color and you will see it!'''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)
        
    @command()
    async def hi(self, ctx):
        await ctx.send("hi.")
        
    @command()
    async def level(self, ctx, name):
      level = hypixel.get_level(name) 
      if level is None:
        e = discord.Embed(title=f"{name}", description=f"Player {name} is not found!, Please make sure to use their **Minecraft** username.")
        await ctx.send(embed=e)
      else:
        e1 = discord.Embed(title=f"Level Of User {name}", description=f"{level}")
        await ctx.send(embed=e1)
          
          
    @command()
    async def gay(self, ctx):
      lis = ["1%", "58%", "32%", "85%", "37%", "48%", "50%"]
      await ctx.send(f"You are {random.choice(lis)} gay")

def setup(bot):
    bot.add_cog(Random(bot))
