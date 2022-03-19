import discord
from discord.ext import commands

from src.scripts.utils.new_owner import new_owner

class LeaveCustomVc(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel != None:
            guild: discord.Guild = member.guild

            try:
                vc_list: list = list(self.client.VoiceChannels[guild.id].keys())

                if before.channel.id in vc_list:
                    if len(before.channel.members) <= 0:
                        await before.channel.delete()

                        self.client.VoiceChannels[guild.id].pop(before.channel.id)

                    else:
                        if member.id == self.client.VoiceChannels[guild.id][before.channel.id]["owner"]:
                            try:self.client.VoiceChannels[guild.id][before.channel.id]["owner"] = new_owner(before.channel).id
                            except: await before.channel.delete()

            except KeyError:
                pass

def setup(client: commands.Bot):
    client.add_cog(LeaveCustomVc(client=client))