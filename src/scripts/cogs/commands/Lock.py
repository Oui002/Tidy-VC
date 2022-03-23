import discord
from discord.ext import commands
from discord.commands import slash_command

class Lock(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(guild_ids=[898532471841378334, 923611569928147014])
    async def lock(self, ctx):
        if ctx.author.voice is not None and isinstance(ctx.author.voice.channel, discord.VoiceChannel):
            channel: discord.VoiceChannel = ctx.author.voice.channel

            if (channel.id in list(self.client.VoiceChannels[channel.guild.id].keys()) 
            and ctx.author.id == self.client.VoiceChannels[channel.guild.id][channel.id]["owner"]):
                await channel.edit(user_limit=len(channel.members))
                await ctx.respond(f"Locked <#{channel.id}>")

def setup(client: commands.Bot):
    client.add_cog(Lock(client=client))