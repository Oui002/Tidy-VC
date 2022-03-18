from discord.ext import commands

from src.scripts.client._class import Cli

def main():
    client = Cli()

    @client.event
    async def on_ready():
        print("Ready!")

    client.print_config()

    client.run(client.token)