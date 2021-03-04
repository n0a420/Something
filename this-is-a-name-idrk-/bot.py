import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '#')
status = (['Status 1', 'Status 2'])

client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='𝐋𝐨𝐮𝐯𝐫é ⛓️'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(next(status)))


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

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

client.run('Token')
