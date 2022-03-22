import discord

def id2vc(guild: discord.Guild, channel_id: int) -> discord.VoiceChannel:
    return discord.utils.find(lambda VoiceChannel: VoiceChannel.id == channel_id, guild.voice_channels)
