import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(898811663678050317)
    await channel.send(F'{member}join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(898811663678050317)
    await channel.send(F'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}(ms)')

bot.run('ODk4ODA5MjYzODczNDc4Njg2.YWpnWw.nYd02elpEPT1nzJZS98-NsmJC-4')