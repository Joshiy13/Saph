from discord.ext import commands


client = commands.Bot()

class Ping(commands.Cog):
    
        def __init__(self, client):
            self.client = client
    
        @client.slash_command(guild_ids=[960188361874747393])
        async def ping(ctx):
            await ctx.respond(f"Pong! {round(client.latency * 1000)}ms")

def setup(client):
    client.add_cog(Ping(client))
