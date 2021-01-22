import discord
import wavelink
from discord.ext import commands





class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        await self.bot.wavelink.initiate_node(host='lavalink.something.host',
                                              port=80,
                                              rest_uri='http://lavalink.something.host:80',
                                              password='youshallnotpass',
                                              identifier='TEST',
                                              region='us_central')
    @commands.command()
    async def vol_up(self, ctx, vol):
        """Command used for volume up button."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.is_connected():
            return

    

        if vol > 100:
            vol = 100
            await ctx.send('Maximum volume reached', delete_after=7)

        await player.set_volume(int(vol))

    @commands.command()
    async def vol_down(self, ctx, vol):
        """Command used for volume down button."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.is_connected():
            return

        if vol < 0:
            vol = 0
            await ctx.send('Player is currently muted', delete_after=10)

        await player.set_volume(int(vol))                                

    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**')
        await player.connect(channel.id)

    @commands.command()
    async def play(self, ctx, *, query: str):
        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

        if not tracks:
            return await ctx.send('Could not find any songs with that query.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        await ctx.send(f'Added {str(tracks[0])} to the queue.')
        await player.play(tracks[0])

def setup(bot):
    bot.add_cog(Music(bot))
