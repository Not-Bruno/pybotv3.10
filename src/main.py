import logging
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO) # ?
log = logging.getLogger('BOT-MAIN') # ?

# Discord Bot definition
bot = commands.Bot(
    command_prefix=None, # Nur / commands
    intents=discord.Intents.default(), # ?
    activity=discord.Activity(type=discord.ActivityType.watching, name="Discord"), # aktivität
    status=discord.Status.online, # online status
    sync_commands=False, # ?
    delete_not_existing_commands=False, # ?
)

if __name__ == "__main__":
    log.info("Starting Discord Bot ...")
    token = os.getenv("BOT_TOKEN")
    bot.run(token=token)