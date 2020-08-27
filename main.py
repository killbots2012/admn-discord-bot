import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio
import os 


client = commands.Bot(command_prefix='t-')
client.remove_command('ping')


#start up
@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}') 
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
       

client.run("NjgzMTA4NTg2NzU4NjAyNzY5.Xlmwcg.UORij7MAJtH87wIKVh2GBGV768s")


