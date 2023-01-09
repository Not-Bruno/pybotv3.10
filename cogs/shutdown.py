# Command -- Shutdown
import discord
from discord.ext impoer commands

class ShutdownCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = Bot

    @commands.Cog.slash_command(name="shutdown", description="Shutdown Bot")
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        embed = discord.Embed(title=f"Bot Notification", color=discord.Color.from_rgb(ffff00))
        embed.add_field(name="Information", value=f"--")

        await bot.close()
        await ctx.respond()
        log.info("Bot Closed ...")

def setup(bot):
	bot.add_cog(ShutdownCommand(bot))