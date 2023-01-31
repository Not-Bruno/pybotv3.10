import asyncio
import logging
import os
from pathlib import Path

import discord
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO) # Log Level INFO
log = logging.getLogger('BOT-MAIN') # Bot logging as BOT-MAIN

# Define Intents
intents = discord.Intents.default()
intents.members = True

# Discord Bot definition
bot = commands.Bot(
	command_prefix=commands.when_mentioned_or(),
	intents=intents,
	activity=discord.Activity(type=discord.ActivityType.playing, name='Hello World!'),
	status=discord.Status.online,
	sync_commands=True,
	delete_not_existing_commands=True
)

if __name__ == '__main__':
	log.info('Starting bot...')
	token = os.getenv('BOT_TOKEN')
	bot.run(token)