import discord
from discord.ext import commands

class Ready(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Online!")


def setup(client: commands.Bot):
    client.add_cog(Ready(client=client))