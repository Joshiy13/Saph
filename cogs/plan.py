import discord
from discord.ext import commands


class Plan(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    


    @discord.slash_command(name= "plan", description="Plan an Event. Usage: /plan <title(scrim or official)> <date(dd/mm/yyyy)> <time(hh:mm)>") 
    async def Lineup(self, ctx, title=None, date=None, time=None, ):
        plan = discord.Embed(title="Game found!", color=0xfa0505)
        plan.add_field(name="Scrim or Match?", value=f"{title}", inline=False)
        plan.add_field(name="Date of Game:", value=f"{date}", inline=False)
        plan.add_field(name="Time of Game:", value=f"{time} CET", inline=False)

        channel = self.bot.get_channel(1110214530686001192)
    
        if title == None or date == None or time == None:
            await ctx.respond("Please enter a title!")
        else:
            await channel.send(embed=plan)
            await ctx.respond("Game planned!")
            
            
    
        
    

def setup(bot): 
    bot.add_cog(Plan(bot)) # this is how we add our cog to the bot