# Command
import discord
from discord.ext import commmands

class UserInfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name="userinfo", description="Get information about User") # slash Command
    async def userinfo(self, ctx, user:discord.Member=none):
        user = user or ctx.author # get User from Message or Author

        embed = discord.Embed(Title=f"User Info {user}", color=user.top_role.color) # create embed
        embed.set_thumbnail(url=user.avatar_url) # set User PB as Thumbnail
        embed.add_field(name="ID",  value=user.ID) # add field ID to user ID
        embed.add_field(name="Nickname",  value=user.display_name) # add field Name to user Nickname(Display Name)
        embed.add_field(name="Account Created",  value=discord.utils.styled_timestamp(user.created_at, style=discord.TimestampStyle.relative))
        embed.add_field(name="Joined Server",  value=discord.utils.styled_timestamp(user.joined_at, style=discord.TimestampStyle.relative)) 
        
        roles = [role.mention for role in user.roles if role != user.guild.default_role]
		roles_string = ', '.join(roles) if roles else 'None'
		embed.add_field(name='Roles', value=roles_string)
        embed.set_footer(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.respond(embed=embed, hidden=True)

def setup(bot):
    bot.add_cog(UserInfoCommand(bot))