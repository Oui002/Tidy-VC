from discord.ext import commands

from json import load

class Cli(commands.Bot):
    
    def __init__(self) -> None:
        self.config = self.load_config()
        super().__init__(command_prefix=self.config["command_prefix"])

        self.token = self.config["client_token"]
        
    def load_config(self) -> object:
        with open('./src/config/cfg.json', 'r+') as fo:
            config = load(fo)
        
        return config

    def print_config(self) -> None:
        print(self.config)