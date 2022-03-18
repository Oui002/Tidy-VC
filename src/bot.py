from discord.ext import commands

from src.scripts.client._class import Cli

def main():
    client = Cli()
    client.load_cogs()
    client.run(client.token)