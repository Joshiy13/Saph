import os
os.system("pip install py-cord==2.0.0b1")
import discord
from discord.ext import commands
import asyncio


client = commands.Bot()
token = "MTA0ODI5NjkwNDc5MTk2NTgxOQ.GTlzdM.gYl-kPTXIiOZUVJlIXoH9sE3vOOieKEf3SgnKg"
intents = discord.Intents.none()
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True
intents.voice_states = True

cogs_list = [
    "ping",
    "test",
    "help",
    "lineup",
    "submit",
]

for cog in cogs_list:
    client.load_extension(f"cogs.{cog}")


@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Bot is ready!")


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author != client.user:
            if message.attachments:
                attachment = message.attachments[0]
                if attachment.filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.avi', '.mkv')):
                    await message.channel.send(f"Thanks for the file {message.author.mention}! I'll send it to the server.")
                    await attachment.save(attachment.filename)
                    message_text = f"{message.author.mention} sends: {message.content}"
                    channel = client.get_channel(1053337652939739196)
                    await channel.send(message_text, file=discord.File(attachment.filename))
                    os.remove(attachment.filename)
                else:
                    # File type is not supported, send a message back to the user
                    await message.channel.send(f"Sorry {message.author.mention}, only image and video file types are supported.")



#Fügt den Status des Bots hinzu
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="/help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Coded by @joshiy13#7277"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="DM to submit lineups"))
        await asyncio.sleep(10)



client.run(token) #runnt den bot