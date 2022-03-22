import atexit
from discord.ext import commands

from asyncio import run
from json import dumps, load

from src.scripts.utils.converters.ID2VoiceChannel import id2vc
from src.scripts.utils.new_owner import new_owner

class CleanUp(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    async def job_start(self):
        with open('./src/save/active_vcs.json', 'r+') as fo:
            data = load(fo)
        with open('./src/save/active_vcs.json', 'w+') as fo:
            fo.write('{}')

        for guild in self.client.guilds:
            try:
                for channel_id in list(data[str(guild.id)]):
                    channel = id2vc(guild, channel_id)

                    if len(channel.members) == 0: await channel.delete()
                    else: self.client.VoiceChannels[guild.id].update({channel.id: {"owner": new_owner(channel=channel).id}})
            except KeyError:
                continue
    
    def job_save(self, args):
        save = {}

        for guild in self.client.guilds:
            try:
                vcs = [key for key in list(args[guild.id].keys())]
                if len(vcs) > 0: save.update({guild.id: vcs})
            except KeyError: continue
            
        with open('./src/save/active_vcs.json', 'w+') as fo:
            fo.write(dumps(save))

    @commands.Cog.listener()
    async def on_ready(self):
        await self.job_start()
        atexit.register(self.job_save, args=self.client.VoiceChannels)

def setup(client: commands.Bot):
    client.add_cog(CleanUp(client=client))