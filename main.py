import discord
from discord.ext import commands
import asyncio
import os

client = commands.Bot()
token = os.getenv("TOKEN")

intents = discord.Intents.none()
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True
intents.voice_states = True
intents.message_content = True

cogs_list = [
    "greetings",


]

for cog in cogs_list:
    client.load_extension(f"cogs.{cog}")


@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Bot is ready!")


#Fügt den Status des Bots hinzu
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="/help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Coded by @joshiy13#7277"))
        await asyncio.sleep(10)



#Fügt einen Slash command hinzu
@client.slash_command(name="test", description="Tests if the Bot is running", guild_ids=[960188361874747393]) # test server guild id must be changed before deployment
async def first_slash(ctx): 
    await ctx.respond("Test completed!")



client.run(token) #runnt den bot