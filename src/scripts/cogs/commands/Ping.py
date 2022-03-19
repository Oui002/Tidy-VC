from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
    
    @commands.slash_command(guild_ids=[923611569928147014, 898532471841378334], name="ping", description="Ping of the bot in ms.")
    async def test(self, ctx):
        await ctx.respond(f"pong! {self.client.latency * 1000}ms")
    
def setup(client: commands.Bot):
    client.add_cog(Ping(client=client))