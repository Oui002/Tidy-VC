from discord.ext import commands

class StartupLog(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print(f"Connected to {self.client.ws}...")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Ready as {self.client.user}!")


def setup(client: commands.Bot):
    client.add_cog(StartupLog(client=client))