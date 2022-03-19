import discord
from discord.ext import commands

class LeaveCustomVc(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before, after):
        if before.channel.id == self.client.current_vc:
            if len(before.channel.members) <= 0:
                await before.channel.delete()

def setup(client: commands.Bot):
    client.add_cog(LeaveCustomVc(client=client))