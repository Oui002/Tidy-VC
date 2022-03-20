from discord.ext import commands

class InitVoiceChannels(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        self.client._VoiceChannels(self.client)

def setup(client: commands.Bot):
    client.add_cog(InitVoiceChannels(client=client))
