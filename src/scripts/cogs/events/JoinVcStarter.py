import discord
from discord.ext import commands

class JoinVcStarter(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if after.channel is not None:
            channel: discord.VoiceChannel = member.voice.channel
            guild_id: int = channel.guild.id

            try: self.client.VCStarterChannels[str(guild_id)]
            except: self.client.VCStarterChannels[str(guild_id)] = None
            self.client.save_vc_starters()

            if channel.id == int(self.client.VCStarterChannels[str(guild_id)]):
                new_channel = await channel.category.create_voice_channel(name=f"{member.name}'s VC")

                try: self.client.VoiceChannels[guild_id]
                except KeyError: self.client.VoiceChannels[guild_id] = {}; 

                self.client.VoiceChannels[guild_id].update({new_channel.id: {"owner": member.id}})
                
                await member.move_to(channel=new_channel)

def setup(client: commands.Bot):
    client.add_cog(JoinVcStarter(client=client))