#Imports
import discord
from discord.ext import commands
import discord.utils
import asyncio
from asyncio import sleep

#Prefix | Removing Default Help Command
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

#Startup Event | Bot Status
@bot.event
async def on_ready():
    print('Bot is online.')
    await bot.change_presence(activity=discord.Game('!help | Bot Name'))

#Setup Cogs
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Ping Command
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong!")

    #Custom Help Command
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="Help Command", color=0x00b3ff)
        embed.add_field(name="❯ Command Category", value="``!command`` ``!command``", inline=False)
        embed.add_field(name="❯ Command Category", value="``!command2`` ``!command2``", inline=False)
        embed.set_footer(text="[Footer Text]")
        await ctx.send(embed=embed)

    #Serverinfo Command
    @commands.command()
    async def serverinfo(self,ctx):
        guild = ctx.guild
        embed=discord.Embed(title="Server Information", color=0x009dff)
        embed.add_field(name="Guild ID:", value=f"{guild.id}", inline=False)
        embed.add_field(name="Server Name:", value=f"{guild.name}", inline=False)
        embed.add_field(name="Server Owner:", value=f"{guild.owner}", inline=False)
        embed.add_field(name="Members:", value=f"{guild.member_count}", inline=False)
        await ctx.send(embed=embed)

    #Formatting Command
    @commands.command()
    async def format(self,ctx, *,text: str):
        channel = bot.get_channel(PASTE CHANNEL ID)
        embed=discord.Embed(title="Formatted Embed", description=f"``{text}``", color=0x00b3ff)
        await channel.send(embed=embed)

#Setup Cogs | Discordbot Token
bot.add_cog(Commands(bot))
bot.run('PASTE TOKEN HERE')