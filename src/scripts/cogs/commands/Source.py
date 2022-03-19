import discord
from discord.ext import commands

class Source(commands.Cog):

    def __init__(self, client) -> None:
        self.client =  client

        self.embed = discord.Embed(color=0x000000)
        self.embed.add_field(name="Github Page", value="[Source Code](https://github.com/oui002/Tidy-VC)")
    
    @commands.command()
    async def source(self, ctx):
        await ctx.reply(embed=self.embed)

def setup(client: commands.Bot):
    client.add_cog(Source(client=client))