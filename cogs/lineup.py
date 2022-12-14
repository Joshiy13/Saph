import discord
from discord.ext import commands


urls = {
    ("bind", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049355111157219408",
    ("bind", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049355132401364992",
    ("bind", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049355303780622397",
    ("bind", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049355717406117908",

    ("bind", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049355841079365763",
    ("bind", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049355858871582801",
    ("bind", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049355873614581871",
    ("bind", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049355893222948894",

    ("haven", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049356246664351835",
    ("haven", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049356262162305084",
    ("haven", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049356279623209030",
    ("haven", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049356292235464754",

    ("haven", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049356311369883818",
    ("haven", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049356328881115176",
    ("haven", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049356345385685042",
    ("haven", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049356363286986884",

    ("haven", "c", "viper"): "https://discord.com/channels/1048302666838724640/1049356382744358962",
    ("haven", "c", "brimstone"): "https://discord.com/channels/1048302666838724640/1049356407436226560",
    ("haven", "c", "kayo"): "https://discord.com/channels/1048302666838724640/1049356420597940234",
    ("haven", "c", "raze"): "https://discord.com/channels/1048302666838724640/1049356432132288593",

    ("split", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049357501704974467",
    ("split", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357517324558387",
    ("split", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049357586530586745",
    ("split", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049357599511957635",

    ("split", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049359436386410516",
    ("split", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357687445524510",
    ("split", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362273472348302",
    ("split", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363302716809308",

    ("ascent", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049359414278225960",
    ("ascent", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357734203629710",
    ("ascent", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049362294309671024",
    ("ascent", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049363283179749376",

    ("ascent", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049359393453506622",
    ("ascent", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357720467292221",
    ("ascent", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362371157700618",
    ("ascent", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363263260987402",

    ("icebox", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049359375589978203",
    ("icebox", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357706697383989",
    ("icebox", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049362348189700166",
    ("icebox", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049363463379628043",
    
    ("icebox", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049359356740771861",
    ("icebox", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357903204724898",
    ("icebox", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362326815514644",
    ("icebox", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363227034800200",

    ("breeze", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049362125702828042",
    ("breeze", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357841087090698",
    ("breeze", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049362652117340230",
    ("breeze", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049363421562404954",

    ("breeze", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049362099178065950",
    ("breeze", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049357804454019082",
    ("breeze", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362630621536358",
    ("breeze", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363551837507654",

    ("fracture", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049362064063344731",
    ("fracture", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049358051204939836",
    ("fracture", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049362762700165271",
    ("fracture", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049363569713618954",

    ("fracture", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049362042966003872",
    ("fracture", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049358037137227776",
    ("fracture", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362740399046708",
    ("fracture", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363605709131786",

    ("pearl", "a", "viper"): "https://discord.com/channels/1048302666838724640/1049362020123811913",
    ("pearl", "a", "brimstone"): "https://discord.com/channels/1048302666838724640/1049358024923414549",
    ("pearl", "a", "kayo"): "https://discord.com/channels/1048302666838724640/1049362972289532024",
    ("pearl", "a", "raze"): "https://discord.com/channels/1048302666838724640/1049363440990421062",

    ("pearl", "b", "viper"): "https://discord.com/channels/1048302666838724640/1049362224478687374",
    ("pearl", "b", "brimstone"): "https://discord.com/channels/1048302666838724640/1049358012621520926",
    ("pearl", "b", "kayo"): "https://discord.com/channels/1048302666838724640/1049362953616490586",
    ("pearl", "b", "raze"): "https://discord.com/channels/1048302666838724640/1049363681345020015",

    # etc.
}

class Lineup(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name= "lineup", description="Gives you a lineup for the map and agent you want") 
    async def Lineup(self, ctx, map=None, site=None, agent=None):

        map = map.lower()
        site = site.lower()
        agent = agent.lower()
        
        if map == None:
            await ctx.respond("Please enter a map!")
        if site == None:
            await ctx.respond("Please enter a site!")
        if agent == None:
            await ctx.respond("Please enter an agent!")

        if (map, site, agent) in urls:
            await ctx.respond(f"You can find the lineup here: {urls[(map, site, agent)]}")
        else:
            await ctx.respond("Invalid combination of map, site, and agent!")

def setup(bot): 
    bot.add_cog(Lineup(bot)) # this is how we add our cog to the bot