import discord
from discord.ext import commands


class Ping(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @discord.slash_command(name="ping", description="Shows the latency of the bot", guild_ids=[960188361874747393]) # test server guild id must be changed before deployment
    async def ping(self, ctx):
        await ctx.respond(f"Latency: {round(self.bot.latency * 1000)}ms")


def setup(bot): 
    bot.add_cog(Ping(bot)) # this is how we add our cog to the bot

