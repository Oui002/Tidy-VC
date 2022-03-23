import discord

def new_owner(channel: discord.VoiceChannel) -> discord.Member:
    hierarchy = {member.top_role.position: member.id for member in channel.members if member.top_role is not None}
    new_owner_id = hierarchy[max(list(hierarchy.keys()))]

    return discord.utils.find(lambda GuildMember: GuildMember.id == new_owner_id, channel.guild.members)
