import discord 
from discord.ext import commands
import random
from dotenv import load_dotenv
from os import getenv

load_dotenv()

#reading jokes from jokes.txt file and storing each line in a list
jokes = []
with open('jokes.txt', encoding="utf-8") as f:
    jokes = [joke.rstrip() for joke in f]

#reading facts from facts.txt file and storing each line in a list
facts = []
with open('facts.txt', encoding="utf-8") as f:
    facts = [fact.rstrip() for fact in f]

#reading motivation from motivation.txt file and storing each line in a list
motivation = []
with open('motivation.txt', encoding="utf-8") as m:
    motivation = [motivations.rstrip() for motivations in m]

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello ' + ctx.author.name +"!")

@bot.command()
async def joke(ctx):
    i = random.randint(0,385)
    await ctx.reply(jokes[i])

@bot.command()
async def fact(ctx):
    i = random.randint(0,100)
    await ctx.reply(facts[i])

@bot.command()
async def motivations(ctx):
    i = random.randint(0,98)
    await ctx.reply(motivation[i])
   
bot.run(getenv('TOKEN'))