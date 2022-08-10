import discord
import discord.ext.commands
from discord.ext import commands

your_bot_prefix = ""
# Your bot prefix

bot = commands.Bot(command_prefix = your_bot_prefix, help_command=None)

token = ''
# Your bot token
# DONT LEAK THE TOKEN TO ANYONE ! THEY CAN GET FULL ACCESS OVER YOUR BOT



# Say command 
@bot.command()
async def say(ctx, message):
  await ctx.send(message)

    
    
bot.run(token)
# VERY IMPORTANT
# Runs the bot 
# DONT LEAK THE TOKEN TO ANYONE ! THEY CAN GET FULL ACCESS OVER YOUR BOT
