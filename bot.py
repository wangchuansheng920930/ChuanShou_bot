import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    channel = bot.get_channel(int(jdata['main_channel']))
    await channel.send(f'>> 傳說機器人運行中 <<')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['main_channel']))
    await channel.send(f'{member} 已加入此伺服器!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['main_channel']))
    await channel.send(f'{member} 已離開此伺服器!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])