import discord
from discord.ext import commands


class Plan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="plan",
        description="Plan an Event. Usage: /plan <title(scrim or official)> <date(dd/mm/yyyy)> <time(hh:mm)>",
    )
    async def Lineup(self, ctx, title=None, date=None, time=None):
        plan = discord.Embed(title="Game found!", color=0xfa0505)
        plan.add_field(name="Scrim or Match?", value=f"{title}", inline=False)
        plan.add_field(name="Date of Game:", value=f"{date}", inline=False)
        plan.add_field(name="Time of Game:", value=f"{time} CET", inline=False)

        channel = self.bot.get_channel(1110214530686001192)
        manager_role_id = 1110220807562600538

        # Check if the command invoker has the manager role
        if discord.utils.get(ctx.author.roles, id=manager_role_id) is None:
            await ctx.respond("You don't have permission to use this command.")
            return

        if title is None or date is None or time is None:
            await ctx.respond("Please enter a title!")
        else:
            await channel.send(embed=plan)
            await ctx.respond("Game planned!")


def setup(bot):
    bot.add_cog(Plan(bot))