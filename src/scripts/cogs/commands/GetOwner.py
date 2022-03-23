import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class GetOwner(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(guild_ids=[898532471841378334, 923611569928147014])
    async def get_owner(self, ctx, channel: Option(discord.VoiceChannel, "The VoiceChannel", required=True)) -> None:
        return (await ctx.respond(f"<@{self.client.VoiceChannels[channel.guild.id][channel.id]['owner']}> is the current owner of <#{channel.id}>") 
        if channel.id in list(self.client.VoiceChannels[channel.guild.id].keys()) 
        else await ctx.respond("Internal error occurred, please try again later."))

def setup(client: commands.Bot):
    client.add_cog(GetOwner(client=client))