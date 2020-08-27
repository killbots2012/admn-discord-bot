import discord
from discord.ext import commands
import random

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Games cog started')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *,question):
        responses =["I don't think so",
                    "Try again later",
                    "I think so?",
                    "I say no",
                    "Totaly",
                    "Ask Hyper he might know",
                    "Maybe next year",
                    "Don't count on it",
                    "It is certain",
                    " It is decidedly so.",
                    "Most likely.",
                    "My sources say no.",
                    "Outlook good.",
                    "Reply hazy, try again.",
                    "Signs point to yes.",
                    "Very doubtful.",
                    "Without a doubt.",
                    "Yes.",
                    "Yes – definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

 

def setup(client):
    client.add_cog(Games(client))