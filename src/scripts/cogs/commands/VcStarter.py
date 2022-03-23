import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class SetVcStarter(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(name="set_starter", description="Sets the VoiceChannel which should be joined to create a custom vc.", guild_ids=[898532471841378334, 923611569928147014])
    async def set_starter(self, ctx, channel: Option(discord.VoiceChannel, "The VoiceChannel", required=True)):
        self.client.VCStarterChannels[str(channel.guild.id)] = str(channel.id)
        await ctx.respond(f"Set the VcStarter to <#{channel.id}>")
        self.client.save_vc_starters()

def setup(client: commands.Bot):
    client.add_cog(SetVcStarter(client=client))