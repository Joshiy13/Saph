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
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355111157219408")
        if map == "bind":
            if site == "a": 
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355132401364992")
        if map == "bind":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355303780622397")
        if map == "bind":
            if site == "a":
                if agent ==  "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355717406117908")
        
        if map == "bind":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355841079365763")
        if map == "bind":
            if site == "b": 
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355858871582801")
        if map == "bind":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355873614581871")
        if map == "bind":
            if site == "b":
                if agent ==  "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049355893222948894")





        if map == "haven":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356246664351835")
        if map == "haven":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356262162305084")
        if map == "haven":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356279623209030")
        if map == "haven":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356292235464754")

        if map == "haven":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356311369883818")
        if map == "haven":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356328881115176")
        if map == "haven":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356345385685042")
        if map == "haven":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356363286986884")

        if map == "haven":
            if site == "c":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356382744358962")
        if map == "haven": 
            if site == "c":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356407436226560")
        if map == "haven":
            if site == "c":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356420597940234")
        if map == "haven":
            if site == "c":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049356432132288593")





        if map == "split":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357501704974467")
        if map == "split":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357517324558387")
        if map == "split":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357586530586745")
        if map == "split":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357599511957635")

        if map == "split":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049359436386410516")
        if map == "split":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357687445524510")
        if map == "split":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362273472348302")
        if map == "split":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363302716809308")


        

        if map == "ascent":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049359414278225960")
        if map == "ascent":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357734203629710")
        if map == "ascent":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362294309671024")
        if map == "ascent":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363283179749376")
        
        if map == "ascent":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049359393453506622")
        if map == "ascent":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357720467292221")
        if map == "ascent":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362371157700618")
        if map == "ascent":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363263260987402")


        

        if map == "icebox":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049359375589978203")
        if map == "icebox":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357706697383989")
        if map == "icebox":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362348189700166")
        if map == "icebox":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363463379628043")
        
        if map == "icebox":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049359356740771861")
        if map == "icebox":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357903204724898")
        if map == "icebox":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362326815514644")
        if map == "icebox":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363227034800200")




        if map == "breeze":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362125702828042")
        if map == "breeze":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357841087090698")
        if map == "breeze":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362652117340230")
        if map == "breeze":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363421562404954")
        
        if map == "breeze":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362099178065950")
        if map == "breeze":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049357804454019082")
        if map == "breeze":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362630621536358")
        if map == "breeze":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363551837507654")




        if map == "fracture":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362064063344731")
        if map == "fracture":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049358051204939836")
        if map == "fracture":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362762700165271")
        if map == "fracture":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363569713618954")
        
        if map == "fracture":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362042966003872")
        if map == "fracture":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049358037137227776")
        if map == "fracture":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362740399046708")
        if map == "fracture":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363605709131786")




        if map == "pearl":
            if site == "a":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362020123811913")
        if map == "pearl":
            if site == "a":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049358024923414549")
        if map == "pearl":
            if site == "a":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362972289532024")
        if map == "pearl":
            if site == "a":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363440990421062")
        
        if map == "pearl":
            if site == "b":
                if agent == "viper":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362224478687374")
        if map == "pearl":
            if site == "b":
                if agent == "brimstone":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049358012621520926")
        if map == "pearl":
            if site == "b":
                if agent == "kayo":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049362953616490586")
        if map == "pearl":
            if site == "b":
                if agent == "raze":
                    await ctx.respond("You can find the lineup here: https://discord.com/channels/1048302666838724640/1049363681345020015")

def setup(bot): 
    bot.add_cog(Lineup(bot)) # this is how we add our cog to the bot