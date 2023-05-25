import discord
from discord.ext import commands
import requests


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="meme", description="Displays a random meme")
    async def meme(self, ctx):
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()
        meme_image = data["url"]

        embed = discord.Embed(title="Random Meme", color=0xfa0505)
        embed.set_image(url=meme_image)
        await ctx.respond(embed=embed)
        return


def setup(bot):
    bot.add_cog(Meme(bot))
