import discord
from discord.ext import commands

class Test(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @discord.slash_command(name="test", description="Just a check if the Bot is running") # we can also add application commands
    async def test(self, ctx):
        await ctx.respond('Test completed!')

def setup(bot): 
    bot.add_cog(Test(bot)) # this is how we add our cog to the bot