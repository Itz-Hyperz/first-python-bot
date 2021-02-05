import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(dsf):
    await dsf.send('Pong!')
    print('Ping command was sent, I responded with "Pong!"')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

client.run('ODA3Mjk0NTcwMzYyMTc1NTMx.YB15qA.9o2rQjlzAsJdJfCL0FO3-DHsiEM')