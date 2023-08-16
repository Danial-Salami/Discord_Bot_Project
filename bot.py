import discord
# import os
from discord.ext import commands
# from keep_alive import keep_alive
import random

class Config:

    token = 'Put your token here'
    prefix = ';;'


intents = discord.Intents.all()
client = commands.Bot(command_prefix=Config.prefix, intents=intents)


@client.event
async def on_ready():
    print('IM ONLINE')


@client.command()
async def cmd(ctx):
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE]
    titles = ["(●'◡'●)", "(❁´◡`❁)", "༼ つ ◕_◕ ༽つ", "(☞ﾟヮﾟ)☞" , "☜(ﾟヮﾟ☜)" , "(⌐■_■)"]
    my_embed = discord.Embed(
        title=random.choice(titles),
        colour=random.choice(colors)
    )
    await ctx.send(embed=my_embed)


@client.command()
async def greet(ctx):
    mention = ctx.author.mention
    await ctx.send(f'>>> Salam {mention}...Chekhabar??')


@client.command()
async def setstatus(ctx, status_type):
    if status_type == 'idle':
        await client.change_presence(status=discord.Status.idle)
        await ctx.send(f'>>> Im Idle')
    elif status_type == 'dnd':
        await client.change_presence(status=discord.Status.dnd)
        await ctx.send(f'>>> Im Busy!!!')
    elif status_type == 'offline':
        await client.change_presence(status=discord.Status.offline)
        await ctx.send(f'>>> GOOD BYE!!!')
    else:
        await client.change_presence(status=discord.Status.online)
        await ctx.send(f'>>> Amade be anjam dasturat.!')


@client.command()
async def setactivity(ctx, activity_type, *, activity_text):
    if activity_type == 'playing':
        await client.change_presence(activity=discord.Game(name=activity_text))
        await ctx.send(f'>>> Daram bazi mikonam')
    elif activity_type == 'streaming':
        await client.change_presence(activity=discord.Streaming(name=activity_text, url='https://twitch.tv/twitch'))
        await ctx.send(f'>>> Daram stream mikonam')
    elif activity_type == 'watching':
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_text))
        await ctx.send(f'>>> Daram film mibinam')
    elif activity_type == 'listening':
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_text))
        await ctx.send(f'>>> Daram ahang gush midam')
    else:
        await ctx.send(f'>>> in kalame ro **``{activity_type}``** dar dastoratam nadaram')


@client.command()
async def clear(ctx, count='1'):
    await ctx.channel.purge(limit=int(count)+1)
    await ctx.send(f'>>> {count} payam ro barat pak kardam.')


# keep_alive()
client.run(Config.token)
