import discord
from discord.ext import commands
from discord.commands import slash_command

class Delete(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @slash_command(guild_ids=[898532471841378334, 923611569928147014])
    async def delete(self, ctx):
        caller: discord.Member = ctx.author
        if not caller.voice is None and isinstance(caller.voice.channel, discord.VoiceChannel):
            channel: discord.VoiceChannel = caller.voice.channel
            print(1)

            if channel.id in list(self.client.VoiceChannels[ctx.guild.id].keys()):
                print(2)
                if caller.id == self.client.VoiceChannels[ctx.guild.id][channel.id]["owner"]:
                    await channel.delete()
                    await ctx.respond("Deleted your custom VoiceChannel!")

                else:
                    await ctx.respond("You are not the owner of the VoiceChannel you are currently in.")

            else:
                await ctx.respond("The VoiceChannel you are in is not a custom one!")

        else:
            await ctx.respond("You are not in a VoiceChannel.")

def setup(client: commands.Bot):
    client.add_cog(Delete(client=client))