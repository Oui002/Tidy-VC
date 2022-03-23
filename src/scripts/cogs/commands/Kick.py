import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Kick(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @slash_command(guild_ids=[923611569928147014, 898532471841378334], name="kick", description="Kick someone from the vc you are currently in, if you are the owner.")
    async def kick(self, ctx, member: Option(discord.Member, "member", required=True)):
        ENABLED = True # better implementation later
        if not ENABLED:
            return await ctx.respond("This command is not enabled in this Guild.")

        caller: discord.Member = ctx.author

        if caller.voice is not None and isinstance(caller.voice.channel, discord.VoiceChannel):
            channel: discord.VoiceChannel = caller.voice.channel

            if channel.id in list(self.client.VoiceChannels[ctx.guild.id].keys()):
                if caller.id == member.id:
                    return await ctx.respond("You can't kick yourself")
                if not member in channel.members:
                    return await ctx.respond(f"This member is not in <#{channel.id}>")

                if caller.id == self.client.VoiceChannels[ctx.guild.id][channel.id]["owner"]:
                    await member.move_to(None)

                else:
                    await ctx.respond(f"You are not the owner of <#{channel.id}>")
            else:
                await ctx.respond(f"<#{channel.id}> is not a custom channel")
        else:
            await ctx.respond("You are not in a VoiceChannel")
    
def setup(client: commands.Bot):
    client.add_cog(Kick(client=client))