import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("pong!")

def setup(client: commands.Bot):
    client.add_cog(Ping(client=client))