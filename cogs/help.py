import discord
from discord.ext import commands

help = discord.Embed(title="Help Page", color=0xfa0505)
help.add_field(name="/help", value="Shows this page", inline=False)
help.add_field(name="/ping", value="Shows the latency of this Bot", inline=False)
help.add_field(name="/src", value="Shows the source code of this Bot", inline=False)
help.add_field(name="/plan", value="Plan an Event", inline=False)



class Help(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @discord.slash_command(name="help", description="Use this command to get help") # test server guild id must be changed before deployment
    async def ping(self, ctx):
        await ctx.respond(embed=help)


def setup(bot): 
    bot.add_cog(Help(bot)) # this is how we add our cog to the bot