import discord
from discord.ext import commands


class Plan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="plan",
        description="Plan an Event. Usage: /plan (Fill out all arguments)",
    )
    async def Plan(self, ctx, title=None, date=None, time=None, games=None, maps=None):
        plan = discord.Embed(title="Game found!", color=0xfa0505)
        plan.add_field(name="Scrim or Match?", value=f"{title}", inline=False)
        plan.add_field(name="Date of Game:", value=f"{date}", inline=False)
        plan.add_field(name="Time of Game:", value=f"{time} CET", inline=False)
        plan.add_field(name="Number of Games:", value=f"{games}", inline=False)
        plan.add_field(name="Maps:", value=f"{maps}", inline=False)

        channel = self.bot.get_channel(1110214530686001192)
        player_role_id = 1110224948334694441
        manager_role_id = 1110220807562600538

        # Check if the command invoker has the manager role
        if discord.utils.get(ctx.author.roles, id=manager_role_id) is None:
            await ctx.respond("You don't have permission to use this command.")
            return

        if title is None or date is None or time is None or games is None or maps is None:
            await ctx.respond("Please enter all arguments!")
        else:
            guild = ctx.guild
            player_role = guild.get_role(player_role_id)
            mention = player_role.mention if player_role else "@player-role"
            content = f"{mention}"

            message = await channel.send(content=content, embed=plan)  # Send content and embed
            await message.add_reaction("✅")  # Add checkmark reaction
            await message.add_reaction("❌")  # Add red cross reaction
            await ctx.respond("Game planned!")


def setup(bot):
    bot.add_cog(Plan(bot))