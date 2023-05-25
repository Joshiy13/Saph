import discord
from discord.ext import commands

help = discord.Embed(title="Help Page", color=0xfa0505)
help.add_field(name="/help", value="Shows this page", inline=False)
help.add_field(name="/ping", value="Shows the latency of this Bot", inline=False)
help.add_field(name="/src", value="Shows the source code of this Bot", inline=False)
help.add_field(name="/plan", value="Plan an Event", inline=False)
help.add_field(name="/coinflip", value="Flip a Coin", inline=False)
help.add_field(name="/tictactoe", value="Play Tic Tac Toe against someone", inline=False)
help.add_field(name="/rps", value="Play Rock Paper Scissors against the Bot", inline=False)
help.add_field(name="/meme", value="Shows a random meme", inline=False)



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="help", description="Use this command to get help")
    async def ping(self, ctx):
        await ctx.respond(embed=help)


def setup(bot): 
    bot.add_cog(Help(bot))