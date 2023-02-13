import discord
import datetime
import time

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
counter = 0
profiles = {}

@client.event
async def on_ready():
    print(f'Bot is ready, logged in as {client.user.name} ({client.user.id})')
    await client.change_presence(activity=discord.Game(name="Logging"))

@client.event
async def on_member_join(member):
    global counter
    counter += 1
    profiles[member.id] = {'name': member.name, 'joined_at': member.joined_at}
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the server!')
    log_event(f'{member.name} joined the server.')

@client.event
async def on_message(message):
    if message.content.startswith('!profile'):
        user_id = message.author.id
        if user_id in profiles:
            profile = profiles[user_id]
            response = f'Name: {profile["name"]}\n'
            response += f'Joined at: {profile["joined_at"]}'
            await message.channel.send(response)
        else:
            await message.channel.send(f'No profile found for {message.author.name}.')
    
    elif message.content.startswith('!backup'):
        if message.author.guild_permissions.administrator:
            export_profiles_to_file()
            log_event(f'{message.author.name} initiated a backup.')
        else:
            await message.channel.send(f'You do not have the necessary permissions to execute that command.')
    
    elif message.content.startswith("!shwlog"):
        if message.author.guild_permissions.administrator:
            with open("log.txt", "r") as log_file:
                log = log_file.read()
                await message.channel.send("```\n" + log + "```")
        else:
            await message.channel.send("You don't have permission to execute this command.")
    
    elif message.content.startswith("!clslog"):
        member = message.guild.get_member(message.author.id)
        if member.guild_permissions.administrator:
            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
            with open("log.txt", "w") as log_file:
                log_file.write("")
            with open("log-{}.txt".format(current_time), "w") as backup_file:
                with open("log.txt", "r") as log_file:
                    log = log_file.read()
                    backup_file.write(log)
            await message.channel.send("The log has been cleared and backed up.")
        else:
            await message.channel.send("You don't have permission to execute this command.")
    
    else:
        current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())
        with open("log.txt", "a") as log_file:
            log_file.write("[{}] {}: {}\n".format(current_time, message.author, message.content))

def export_profiles_to_file():
    with open('profiles.txt', 'w') as f:
        for user_id, profile in profiles.items():
            f.write(f'{user_id}:{profile["name"]}:{profile["joined_at"].isoformat()}\n')

def import_profiles_from_file():
    global profiles
    profiles = {}
    try:
        with open('profiles.txt', 'r') as f:
            for line in f:
                user_id, name, joined_at = line.strip().split(':')
                profiles[user_id] = {'name': name, 'joined_at': datetime.datetime.fromisoformat(joined_at)}
    except FileNotFoundError:
        pass

def log_event(event):
    with open('log.txt', 'a') as f:
        f.write(f'[{datetime.datetime.now().isoformat()}] {event}\n')

client.run('token')