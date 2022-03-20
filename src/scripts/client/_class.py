from discord import Intents
from discord.ext import commands

from os import listdir

from json import dumps, load

class Cli(commands.Bot):
    
    def __init__(self) -> None:
        intents = Intents.default()
        intents.message_content=True
        intents.members=True

        self.config = self.load_config()
        super().__init__(command_prefix=self.config["command_prefix"], intents=intents)
        self.token = self.config["client_token"]
        self.load_vc_starters()
        
    def load_config(self) -> object:
        with open("./src/config/cfg.json", "r+") as fo:
            config = load(fo)
        
        return config
    
    def load_vc_starters(self) -> None:
        with open("./src/config/VCStarters.json") as fo:
            self.VCStarterChannels = load(fo)
    
    def save_vc_starters(self) -> None:
        with open("./src/config/VCStarters.json", "w") as fo:
            fo.write(dumps(self.VCStarterChannels))
    
    def load_cogs(self) -> None:
        for folder in listdir("./src/scripts/cogs"):
            for cog_file in listdir(f"./src/scripts/cogs/{folder}"):
                if cog_file.endswith(".py"):
                    self.load_extension(f"src.scripts.cogs.{folder}.{cog_file[:-3]}")
    
    def _VoiceChannels(self, client) -> None:
        self.VoiceChannels = {}
        
        for guild in client.guilds:
            self.VoiceChannels[guild.id] = {}