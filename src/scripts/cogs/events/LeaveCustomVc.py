import discord
from discord.ext import commands

class LeaveCustomVc(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel != None:
            try:
                guild_vc_list = self.client.VoiceChannels[before.channel.guild.id]

                if before.channel.id in guild_vc_list:
                    if len(before.channel.members) <= 0:
                        await before.channel.delete()

            except KeyError:
                pass

def setup(client: commands.Bot):
    client.add_cog(LeaveCustomVc(client=client))