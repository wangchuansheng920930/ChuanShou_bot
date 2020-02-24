import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):


    @commands.command()
    async def sy(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def un(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def sp(self, ctx):
        await ctx.send(f'{self.bot.latency} (s)')

    @commands.command()
    async def about(self, ctx):
        await ctx.send('關於機器:傳說機器人V1.0\n作者:傳說\n機器版本:1.0\n運行狀態:運行中\n機器測速:可以執行\n進群提醒:可以執行\n退群提醒:可以執行')

    @commands.command()
    async def set(self, ctx):
        embed=discord.Embed(title="作者FaceBook", url="https://www.facebook.com/profile.php?id=100016471382698", description="王傳昇", color=0x258fc2)
        embed.set_author(name="作者LINE", url="http://line.me/ti/p/wang651215", icon_url="https://scontent.frmq2-1.fna.fbcdn.net/v/t1.0-9/83425200_597703980788643_6322350172206530560_n.jpg?_nc_cat=110&_nc_ohc=VuXCNYewHk0AX8uRcMU&_nc_ht=scontent.frmq2-1.fna&oh=5383c7a7552d4db0968c058a0055e1de&oe=5EF3C956")
        embed.set_thumbnail(url="https://scontent.frmq2-1.fna.fbcdn.net/v/t1.15752-9/87348766_915775062159219_1045931129074352128_n.jpg?_nc_cat=106&_nc_ohc=ybPYSOADTM4AX_SdcuH&_nc_ht=scontent.frmq2-1.fna&oh=a65ecc2e90a1e91929797ed33834be6a&oe=5EC6E71C")
        embed.add_field(name="使用者權限", value="已啟動☑️", inline=False)
        embed.add_field(name="機器測速", value="已啟動☑️", inline=False)
        embed.add_field(name="伺服器提醒", value="已啟動☑️", inline=False)
        embed.add_field(name="機器名稱:", value="傳說機器人", inline=True)
        embed.add_field(name="作者名稱:", value="王傳昇", inline=True)
        embed.add_field(name="DC名稱:", value="􂤁􀅉􂤁𝓒𝓱𝓾𝓪𝓷𝓢𝓱𝓸𝓾􂤁􀅉􂤁", inline=True)
        embed.add_field(name="DC編號:", value="(#)1488", inline=True)
        embed.add_field(name="販售項目1", value="LineBOT:V4.貪婪.COCO.JS", inline=True)
        embed.add_field(name="販售項目2", value="DiscordBOT 防/翻", inline=True)
        embed.set_footer(text="購買私Line LineID:wang651215")
        await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(Main(bot))