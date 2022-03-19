import discord
from discord.ext import commands

class JoinVcStarter(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel is None and after.channel is not None:
            channel: discord.VoiceChannel = member.voice.channel
            guild_id: int = channel.guild.id

            if channel.id == 954509385059688509:
                new_channel = await channel.category.create_voice_channel(name="unnamed-voicechannel")

                try: self.client.VoiceChannels[guild_id]
                except KeyError: self.client.VoiceChannels[guild_id] = []; 
                guild_vc_list: list = self.client.VoiceChannels[guild_id]; guild_vc_list.append(new_channel.id); self.client.VoiceChannels[guild_id] = guild_vc_list
                
                await member.move_to(channel=new_channel)

def setup(client: commands.Bot):
    client.add_cog(JoinVcStarter(client=client))