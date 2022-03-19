import discord

from src.scripts.converters.ID2GuildMember import ID2GM

def new_owner(channel: discord.VoiceChannel) -> discord.Member:
    guild = channel.guild

    hierarchy = {member.id: member.top_role.position for member in channel.members}
    highest_ranking = 0

    for member_id in list(hierarchy.keys()):
        try:
            if hierarchy[member_id] > highest_ranking:
                highest_ranking = member_id
        except:
            break

    return ID2GM(guild=guild, member_id=highest_ranking)
