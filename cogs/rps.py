import discord
from discord.ext import commands
import random

class Rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rps", description="Play Rock Paper Scissors against the Bot")
    async def play_rps(self, ctx, pick=None):
        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)

        if pick is None:
            await ctx.respond("Please enter your choice!")
            return
        elif pick.lower() not in options:
            await ctx.respond("Please enter a valid choice!")
            return
        else:
            await ctx.respond(f"You chose {pick} and I chose {bot_choice}.")
            if pick.lower() == bot_choice:
                await ctx.send("It's a tie!")
                return
            elif pick.lower() == "rock":
                if bot_choice == "paper":
                    await ctx.send("I win!")
                    return
                else:
                    await ctx.send("You win!")
                    return
            elif pick.lower() == "paper":
                if bot_choice == "scissors":
                    await ctx.send("I win!")
                    return
                else:
                    await ctx.send("You win!")
                    return
            elif pick.lower() == "scissors":
                if bot_choice == "rock":
                    await ctx.send("I win!")
                    return
                else:
                    await ctx.send("You win!")
            return
            

def setup(bot):
    bot.add_cog(Rps(bot))