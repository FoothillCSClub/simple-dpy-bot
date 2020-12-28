from discord.ext import commands

import aiohttp

from random import randint
import pprint
from os import getenv

bot = commands.Bot(
    command_prefix='prefix '
)
# 5
bot.http_session = aiohttp.ClientSession()

# 1


@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} with user ID {bot.user.id} is ready to use!')

# 3


@bot.event
async def on_message(message):
    if 'heck' in message.content:
        await message.channel.send('That is not appropriate!')

# 2


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# 4


@bot.command()
async def roll(ctx, amount: int):
    roles = [randint(1, 6) for _ in range(amount)]

    await ctx.send(f'Dice rolled {amount} times. Average: {sum(roles) / amount}.')

# 6


@bot.command()
async def reddit(ctx, subreddit):
    async with bot.http_session.get('https://www.reddit.com/r/Eyebleach/top/.json?t=day') as resp:
        if resp.status != 200:
            await ctx.send(f'Something went wrong! Status code {resp.status}')
            return
        else:
            json = await resp.json()
            pprint(json)

bot.run(getenv('TOKEN'), bot=True, reconnect=True)
