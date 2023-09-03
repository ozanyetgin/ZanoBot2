import discord
from discord.ext import commands
import random
import string

from pass_gen_func import pass_gen
from settings import settings
from eglence_logic import *


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim

intents.message_content = True

# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Kaliteye hoş geldiniz...')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')

@bot.command()
async def spotify(ctx):
    await ctx.send(f'https://open.spotify.com/playlist/2iBNDKyTDyV5o5YdvQ9MOy?si=bc4403ea7db54904')

@bot.command()
async def parola(ctx):
    await ctx.send("**10 Haneli Parolanız:** `"+pass_gen(10)+"`")

@bot.command()
async def yazıtura(ctx):
    await ctx.send(yazitura())

@bot.command()
async def emoji(ctx):
    await ctx.send(randomemoji())


bot.run(settings["TOKEN"])