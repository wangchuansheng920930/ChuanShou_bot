import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='//')

@bot.event
async def on_ready():
    channel = bot.get_channel(680753558961913866)
    await channel.send(f'>> 傳說機器人已成功運行 <<')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(680753558961913866)
    await channel.send(f'{member} 已加入此伺服器!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(680753558961913866)
    await channel.send(f'{member} 已離開此伺服器!')

@bot.command()
async def sp(ctx):
    await ctx.send(f'{bot.latency} (s)')




bot.run('NjgwOTY4MTYzNTIwNjc2MDIw.XlHsfw.2lfTPdvFZoF9HYHAZ28sBCCK0gg')