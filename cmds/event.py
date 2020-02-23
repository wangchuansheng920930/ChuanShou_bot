import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['main_channel']))
        await channel.send(f'{member} 已加入此伺服器!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['main_channel']))
        await channel.send(f'{member} 已離開此伺服器!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['作者', '機器']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('機器作者:傳說\nDC名稱:􂤁􀅉􂤁𝓒𝓱𝓾𝓪𝓷𝓢𝓱𝓸𝓾􂤁􀅉􂤁\n帳號編號:#1488\n好友搜尋:􂤁􀅉􂤁𝓒𝓱𝓾𝓪𝓷𝓢𝓱𝓸𝓾􂤁􀅉􂤁#1488')

def setup(bot):
    bot.add_cog(Event(bot))