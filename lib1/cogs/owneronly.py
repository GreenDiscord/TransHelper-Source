               "ratty",
               "chivalrous",
               "didactic",
               "sticky",
               "amuck",
               "supreme",
               "polite",
               "abnormal",
               "hilarious",
               "vacuous",
               "enchanted",
               "real",
               "shaky",
               "infamous",
               "successful",
               "royal",
               "ablaze",
               "delightful",
               "miscreant",
               "flawless",
               "dynamic",
               "woebegone",
               "oopsided",
               "old",
               "acid",
               "vagabond",
               "level"]
        channel = self.bot.get_channel(int(idd))
        await channel.send(f"{message}")
        await ctx.send(f"Your message {message} was sent!")
        await channel.send(f"random word of this message = {random.choice(lis)}")


def setup(bot):
    bot.add_cog(OwnerOnly(bot))
