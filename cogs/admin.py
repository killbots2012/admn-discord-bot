import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin cog started')
    # Welcome/removal statements
    @commands.Cog.listener()
    async def on_member_join(self, client, member):
        await client.get_channel(661060275365216289).send(f"{member.mention} has joined")

    @commands.Cog.listener()
    async def on_member_remove(self, client, member):
        await client.get_channel(661060275365216289).send(f"{member.mention} has remove")

    @commands.command()
    async def clear(self, ctx,amount=3):
       await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
       await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'was {member.mention} banned for: {reason}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await  ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention}: was unbanned')
                return

    @commands.command()
    async def ping (self, ctx):
        await ctx.channel.send(f'Pong! {round(self.client.latency * 1000)}ms')   

    

                        

def setup(client):
    client.add_cog(Admin(client))  