import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class SetVoiceChannelLimit(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(guild_ids=[923611569928147014, 898532471841378334], name="limit", description="Limit the amount of people that can join this channel.")
    async def limit(self, ctx, value: Option(int, "limit", min_value=0, required=True)):
        caller: discord.Member = ctx.author

        if caller.voice is not None and isinstance(caller.voice.channel, discord.VoiceChannel):
            channel: discord.VoiceChannel = caller.voice.channel

            if channel.id in list(self.client.VoiceChannels[ctx.guild.id].keys()):
                if caller.id == self.client.VoiceChannels[ctx.guild.id][channel.id]["owner"]:
                    if value > 99:
                        value = 0

                    await channel.edit(user_limit=value)

                    await ctx.respond("Changed <#{}>'s limit to {}".format(channel.id, value if value > 0 and value < 100 else "infinity"))
                    
                else:
                    await ctx.respond(f"You are not the owner of <#{channel.id}>")
            else:
                await ctx.respond(f"<#{channel.id}> is not a custom channel")
        else:
            await ctx.respond("You are not in a VoiceChannel")

def setup(client: commands.Bot):
    client.add_cog(SetVoiceChannelLimit(client=client))