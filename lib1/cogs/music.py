from discord.ext import commands
import lavalink
from discord import utils
from discord import Embed
import discord
import math
import re

class MusicCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.music = lavalink.Client(self.bot.user.id)
    self.bot.music.add_node('lavalink.something.host', 80, 'youshallnotpass', 'na', 'music-node')
    self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
    self.bot.music.add_event_hook(self.track_hook)
  
  
  
  @commands.command(name='join')
  async def join(self, ctx):
    print('join command worked')
    member = utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
    if member is not None and member.voice is not None:
      vc = member.voice.channel
      player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
      if not player.is_connected:
        player.store('channel', ctx.channel.id)
        await self.connect_to(ctx.guild.id, str(vc.id))
        e = discord.Embed(title="Joined Voice Channel", description=f"Joined Voice Channel {vc}")
        await ctx.send(embed=e)
      else:
        await ctx.send("I'm already connected!")
  
  
    @commands.command(name='skip', aliases=['s'])
    @commands.guild_only()
    async def _skip(self, ctx):
        """ Skips the current track. """
        player = self.bot.music.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('Not playing.')

        await player.skip()
        await ctx.send('⏭ | Skipped.')
      
    
  @commands.command(name="queue", aliases=["q"])
  async def queue(self, ctx):
    """Display queue [q]"""
    player = self.bot.music.player_manager.get(ctx.guild.id)
    
    
    desc = ""
	
    if (len(player.queue) == 0 and not(player.current)):
      desc = "Empty Queue"
      await ctx.send(f"{desc}")
    else:
      desc = "1. " + player.current.title
      for i in range(0, len(player.queue)):
        desc = desc + '\n' + str(i+2) + ". " + player.queue[i].title
        e = discord.Embed(title="Queue", description=f"{desc}")
    await ctx.send(embed=e)
        
  @commands.command(name='now', aliases=['np', 'n', 'playing'])
  @commands.guild_only()
  async def _now(self, ctx):
        """ Shows some stats about the currently playing song. """
        player = self.bot.music.player_manager.get(ctx.guild.id)
        song = 'Nothing'

        if player.current:
            position = lavalink.Utils.format_time(player.position)
            if player.current.stream:
                duration = '🔴 LIVE'
            else:
                duration = lavalink.Utils.format_time(player.current.duration)
            song = f'**[{player.current.title}]({player.current.uri})**\n({position}/{duration})'

        embed = discord.Embed(color=discord.Color.blurple(),
                              title='Now Playing', description=song)
        await ctx.send(embed=embed)     
  @commands.command(name="remove", aliases=["r"])
  async def remove(self, ctx, idx):
    """[idx] - Remove song with given index from queue [r]"""
    player = self.bot.music.player_manager.get(ctx.guild.id)
    
    try:
      idx = int(idx) 
    
    except ValueError:
      e1 = discord.Embed(title="Enter index of song", color = discord.Color.red())
      return await ctx.send(embed=e1)
      
    if ((idx < 1) or (idx > len(player.queue)+1)):
      e2 = discord.Embed(title="Enter proper index", color=discord.Color.red())
      return await ctx.send(embed=e2)
        
    if not player.current:
      e3 = discord.Embed(title="Empty queue", color=discord.Color.red())
      return await ctx.send(embed=e3)
        
    if (idx == 1):
      removed = player.current.title
      await player.skip()

		
    else:
      removed = player.queue[idx-2].title
      del player.queue[idx-2]
      e4 = discord.Embed(title=remove + " removed", color = discord.Color.green())
      await ctx.send(embed=e4)
  
        
  @commands.command(name='leave')
  async def leavevoice(self,ctx):
    player = self.bot.music.player_manager.get(ctx.guild.id)
    await self.connect_to(ctx.guild.id, None)
    e = discord.Embed(title="Left Channel", description="Left Voice Channel!")
    await ctx.send(embed=e)
    player.queue.clear()
    
  @commands.command(name='pause', aliases=["ts"])
  async def commanda(self, ctx):
    player = self.bot.music.player_manager.get(ctx.guild.id)
    if player.is_playing:
      await player.set_pause(True)
      e = discord.Embed(title="Paused", description=f"Paused The Current Song")
      await ctx.send(embed=e)
    else:
      await ctx.send("Im not in a channel dummy")
  
  @commands.command(name='unpause', aliases=["up"])
  async def commandb(self, ctx):
    player = self.bot.music.player_manager.get(ctx.guild.id)
    await player.set_pause(False)
    e = discord.Embed(title="Unpaused", description="Unpaused The Current Song")
    await ctx.send(embed=e)
 
  @commands.command(name='volume', aliases=['v'])
  @commands.guild_only()
  async def _volume(self, ctx, volume: int = None):
    """ Changes the player's volume. Must be between 0 and 1000. Error Handling for that is done by Lavalink. """
    player = self.bot.music.player_manager.get(ctx.guild.id)
    
    if not volume:
      return await ctx.send(f'🔈 | {player.volume}%')

    await player.set_volume(volume)
    await ctx.send(f'🔈 | Set to {player.volume}%')
  
  @commands.command(name='stop')
  async def commandc(self, ctx):
    player = self.bot.music.player_manager.get(ctx.guild.id)
    
    if player.is_playing:
      e = discord.Embed(title="Stopped", description=f"Stopped Playing and Left Channel")
      await ctx.send(embed=e)
      await player.stop()
      await self.connect_to(ctx.guild.id, None)
      
    else:
      await ctx.send("Im not playing anything?")
      
  
    
  @commands.command(name='play')
  async def play(self, ctx, *, query):
    try:
      player = self.bot.music.player_manager.get(ctx.guild.id)
      query2 = f'ytsearch:{query}'
      results = await player.node.get_tracks(query2)
      tracks = results['tracks'][0:10]
      i = 0
      query_result = ''
      for track in tracks:
        i = i + 1
        query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'
      embed = Embed()
      embed.description = query_result

      await ctx.channel.send(embed=embed)

      def check(m):
        return m.author.id == ctx.author.id
      
      response = await self.bot.wait_for('message', check=check)
      track = tracks[int(response.content)-1]

      player.add(requester=ctx.author.id, track=track)
      if not player.is_playing:
        await player.play()
        await ctx.send(f"Playing {query} - {response}")

    except Exception as error:
      print(error)
  
  async def track_hook(self, event):
    if isinstance(event, lavalink.events.QueueEndEvent):
      guild_id = int(event.player.guild_id)
      await self.connect_to(guild_id, None)
      
  async def connect_to(self, guild_id: int, channel_id: str):
    ws = self.bot._connection._get_websocket(guild_id)
    await ws.voice_state(str(guild_id), channel_id)
    
def setup(bot):
  bot.add_cog(MusicCog(bot))