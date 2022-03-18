from discord.ext import commands

from os import listdir

from json import load

class Cli(commands.Bot):
    
    def __init__(self) -> None:
        self.config = self.load_config()
        super().__init__(command_prefix=self.config["command_prefix"])

        self.token = self.config["client_token"]
        
    def load_config(self) -> object:
        with open("./src/config/cfg.json", "r+") as fo:
            config = load(fo)
        
        return config
    
    def load_cogs(self) -> None:
        for folder in listdir("./src/scripts/cogs"):
            for cog_file in listdir(f"./src/scripts/cogs/{folder}"):
                if cog_file.endswith(".py"):
                    self.load_extension(f"src.scripts.cogs.{folder}.{cog_file[:-3]}")