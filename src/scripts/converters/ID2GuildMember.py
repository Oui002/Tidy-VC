import discord

def ID2GM(guild: discord.Guild, member_id: int) -> discord.Member:
    return discord.utils.find(lambda GuildMember: GuildMember.id == member_id, guild.members)