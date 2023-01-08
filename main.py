import logging
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO) # Log Level INFO
log = logging.getLogger('BOT-MAIN') # Bot logging as BOT-MAIN

# Define Intents
intents = discord.Intents.default()
intents.members = True

# Discord Bot definition
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(), # Nur / commands
    intents=intents, # ?
    activity=discord.Activity(type=discord.ActivityType.watching, name="Discord"), # aktivität
    status=discord.Status.online, # online status
    sync_commands=True, # ?
    delete_not_existing_commands=True, # ?
)

if __name__ == "__main__":
    log.info("Starting Discord Bot ...")

    log.info('Loading cogs...')
    cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
    log.info(f'Loading {len(cogs)} cogs ...')

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        log.info(f'Loaded cog {cog}')

    token = os.getenv("BOT_TOKEN")
    bot.run(token=token)