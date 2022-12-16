import discord
from discord.ext import commands

submit = discord.Embed(title="Help Page", color=0xfa0505)
submit.add_field(name="How to submit Lineups", value="You can dm the Bot a lineup to submit it. Please write a small text description in the style of 'Haven; A; Viper' and send the lineup in a video of you performing it and a screenshot of the point you need to aim at. If the image size is above 8 MB please use websites like https://www.veed.io/video-compressor to compress it", inline=False)



class Submit(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @discord.slash_command(name="submit", description="Use this command for info on Lineup submission") # test server guild id must be changed before deployment
    async def ping(self, ctx):
        await ctx.respond(embed=submit)


def setup(bot): 
    bot.add_cog(Submit(bot)) # this is how we add our cog to the bot