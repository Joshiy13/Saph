import discord
from discord.ext import commands


class Src(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="src", description="Shows the source code of SAPH")
    async def src(self, ctx):
        await ctx.respond("https://github.com/Joshiy13/Saph")


def setup(bot): 
    bot.add_cog(Src(bot))