import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='t-')

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

   
@client.event
async def on_member_join(member):
   await client.get_channel(661060275365216289).send(f"{member.mention} has joined")
   

@client.event
async def on_member_remove(member):
   await client.get_channel(661060275365216289).send(f"{member.mention} left, fuk u")

@client.command()
async def ping (ctx):
   await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *,question):
    responses =["I don't think so",
                "Try again later",
                "I think so?",
                "I say no",
                "Totaly",
                "Ask Hyper he might know",
                "Maybe next year"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx,amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'was {member.mention} banned for: {reason}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await  ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention}: was unbanned')
            return


client.run("BOT TOKEN HERE")

