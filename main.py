from discord.ext import commands

from os import getenv

import aiohttp

from random import choice

bot = commands.Bot(
    command_prefix='charles '
)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user.name}')

    bot.http_session = aiohttp.ClientSession()

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}')

@bot.command()
async def reddit(ctx, subreddit):
    async with bot.http_session.get(f'https://www.reddit.com/r/{subreddit}/top/.json?t=day&limit=10') as resp:
        if resp.status != 200:
            await ctx.send(f'Oh no, an error occured! Status code: {resp.status}.')
            return

        json = await resp.json()
        data = json['data']['children']
        await ctx.send(choice(data)['data']['url'])


bot.run(getenv('TOKEN'))
