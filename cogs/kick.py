import discord
from discord.ext import commands

class Kick(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @discord.slash_command(description="Kicks a User!")
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        await member.kick()
        await ctx.respond(f'User has been kicked for {reason}!')

def setup(bot): 
    bot.add_cog(Kick(bot)) # this is how we add our cog to the bot