import discord
from discord.ext import commands

class JoinVcStarter(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before, after):
        if before.channel is None and after.channel is not None:
            channel: discord.VoiceChannel = member.voice.channel

            if channel.id == 954509385059688509: # per server defined channel ID
                new_channel = await channel.category.create_voice_channel(name="unnamed-voicechannel")
                # for simplicity sake, aka my brain for right now it'll work like this as it's still in testing and I'm lazy.
                self.client.current_vc = new_channel.id # later this might be an ID that could be converted to a channel object because storing a whole class takes up me memory mate.

                await member.move_to(channel=new_channel)

def setup(client: commands.Bot):
    client.add_cog(JoinVcStarter(client=client))