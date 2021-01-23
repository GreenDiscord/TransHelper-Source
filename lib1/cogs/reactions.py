import discord
from discord.ext import commands
  
from datetime import datetime, timedelta
from random import choice

from discord.ext.commands import Cog



class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.db = bot.db
        self.cur = self.db.cursor()

    def record(command, *values):
        self.cur.execute(command, tuple(values))

        return cur.fetchone()

    @Cog.listener()
	async def on_raw_reaction_add(self, payload):
            cursor = self.bot.db.cursor()
            if payload.emoji.name == "⭐":
                message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

                if notpayload.member.id != message.author.id:
                    await self.db.execute("SELECT StarMessageID, Stars FROM starboard WHERE RootMessageID = ?", (message.id) or (None, 0)
		    msg_id, stars = cursor.fetchone()

                    embed = discord.Embed(title="Starred message",
                                colour=message.author.colour,
                                timestamp=datetime.utcnow())

                    fields = [("Author", message.author.mention, False),
                            ("Content", message.content or "See attachment", False),
                            ("Stars", stars+1, False)]

                    for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)

                    if len(message.attachments):
                        embed.set_image(url=message.attachments[0].url)

                    if not stars:
                        star_message = await self.starboard_channel.send(embed=embed)
                        cursor.execute("INSERT INTO starboard (RootMessageID, StarMessageID) VALUES (?, ?)",
                                message.id, star_message.id)

                    else:
                        star_message = await self.starboard_channel.fetch_message(msg_id)
                        await star_message.edit(embed=embed)
                        cursor.execute("UPDATE starboard SET Stars = Stars + 1 WHERE RootMessageID = ?", message.id)

                else:
                    await message.remove_reaction(payload.emoji, payload.member)

    

def setup(bot):
    bot.add_cog(Reactions(bot))
