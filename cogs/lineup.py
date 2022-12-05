import discord
from discord.ext import commands

class Lineup(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name= "lineup", description="Gives you a lineup for the map and agent you want") 
    async def Lineup(self, ctx, map=None, site=None, agent=None):
        if map == None:
            await ctx.respond("Please enter a map!")
        if site == None:
            await ctx.respond("Please enter a site!")
        if agent == None:
            await ctx.respond("Please enter an agent!")

        if map == "bind":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662432")
        if map == "bind":
            if site == "a": 
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662433")
        if map == "bind":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662434")
        if map == "bind":
            if site == "a":
                if agent ==  "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662435")
        
        if map == "bind":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662437")
        if map == "bind":
            if site == "b": 
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662438")
        if map == "bind":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662439")
        if map == "bind":
            if site == "b":
                if agent ==  "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094508478484")





        if map == "haven":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")

        if map == "haven":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")

        if map == "haven":
            if site == "c":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven": 
            if site == "c":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "c":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "haven":
            if site == "c":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")





        if map == "split":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")

        if map == "split":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "split":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")


        

        if map == "ascent":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        
        if map == "ascent":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "ascent":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")


        

        if map == "icebox":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        
        if map == "icebox":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "icebox":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")




        if map == "breeze":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        
        if map == "breeze":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "breeze":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")




        if map == "fracture":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        
        if map == "fracture":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "fracture":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")




        if map == "pearl":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        
        if map == "pearl":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")
        if map == "pearl":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1049366093543788655/1049366094210662441")

def setup(bot): 
    bot.add_cog(Lineup(bot)) # this is how we add our cog to the bot