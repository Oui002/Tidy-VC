from discord.ext import commands

class CooldownError(commands.Cog):
    
    def __init__(self, client) -> None:
        self.client = client
        
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(error)

def setup(client: commands.Bot):
    client.add_cog(CooldownError(client=client))