import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

# Events
        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is ready.')

# Commands
        @commands.command()
        async def ping(self, ctx):
            await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client))
