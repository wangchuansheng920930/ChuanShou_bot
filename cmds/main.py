import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):


    @commands.command()
    async def sp(self, ctx):
        await ctx.send(f'{self.bot.latency} (s)')

    @commands.command()
    async def about(self, ctx):
        await ctx.send('關於機器:傳說機器人V1.0\n作者:傳說\n機器版本:1.0\n運行狀態:運行中\n機器測速:可以執行\n進群提醒:可以執行\n退群提醒:可以執行')

def setup(bot):
    bot.add_cog(Main(bot))