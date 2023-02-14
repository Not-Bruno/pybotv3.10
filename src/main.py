import discord
from discord.ext import commands
import youtube_dl

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="with YouTube videos"))

@bot.command(name='yl')
async def yl(ctx, url):
    try:
        ydl_opts = {'outtmpl': '%(id)s%(ext)s'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)

        await ctx.send(f'Here is your video: {filename}', file=discord.File(filename))

        with open('counter.txt', 'a') as f:
            f.write(f'{url}:1\n')

        await ctx.send('Your video has been downloaded!')

        # delete file after 5 minutes
        await asyncio.sleep(300)
        os.remove(filename)

    except Exception as e:
        error_message = f'Error: {str(e)}'
        with open('log.txt', 'a') as f:
            f.write(error_message + '\n')
        await ctx.send('An error occurred while trying to download your video.')
        
@bot.command(name='downloads')
async def downloads(ctx):
    with open('counter.txt', 'r') as f:
        counters = f.readlines()

    counter_dict = {}
    for counter in counters:
        link, count = counter.strip().split(':')
        counter_dict[link] = int(count)

    sorted_counters = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    
    embed = discord.Embed(title="Download Count", color=discord.Color.green())
    for link, count in sorted_counters:
        embed.add_field(name=link, value=count, inline=False)
    
    await ctx.send(embed=embed)

bot.run(TOKEN)