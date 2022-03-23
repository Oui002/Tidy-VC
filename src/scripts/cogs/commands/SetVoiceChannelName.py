import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class SetVoiceChannelName(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(guild_ids=[923611569928147014, 898532471841378334], name="name", description="Set the name of your current voice state channel, if you are the owner.")
    async def name(self, ctx, channel_name: Option(str, "name", required=True)):
        caller: discord.Member = ctx.author
        if caller.voice is not None and isinstance(caller.voice.channel, discord.VoiceChannel):
            channel: discord.VoiceChannel = caller.voice.channel

            if channel.id in list(self.client.VoiceChannels[ctx.guild.id].keys()):
                if caller.id == self.client.VoiceChannels[ctx.guild.id][channel.id]["owner"]:
                    if not channel_name in [channel.name for channel in ctx.guild.channels]:
                        await channel.edit(name=channel_name)
                        await ctx.respond(f"Changed the VoiceChannel's name to <#{channel.id}>")
                    
                    else:
                        await ctx.respond("A channel with this name already exists.")

                else:
                    await ctx.respond("You are not the owner of the VoiceChannel you are currently in.")

            else:
                await ctx.respond("The VoiceChannel you are in is not a custom one!")

        else:
            await ctx.respond("You are not in a VoiceChannel.")

def setup(client: commands.Bot):
    client.add_cog(SetVoiceChannelName(client=client))