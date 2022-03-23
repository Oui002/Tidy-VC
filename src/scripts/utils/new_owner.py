import discord

def new_owner(channel: discord.VoiceChannel) -> discord.Member:
    hierarchy = {member.id: member.top_role.position for member in channel.members}
    highest_ranking = 0

    for member_id in list(hierarchy.keys()):
        if hierarchy[member_id] > highest_ranking:
            highest_ranking = member_id

    return discord.utils.find(lambda GuildMember: GuildMember.id == member_id, channel.guild.members)
