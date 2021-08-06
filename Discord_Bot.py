import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'Connected to guilds: {client.guilds}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Hi":
        await message.channel.send("Go die you piece of black **it")
    if message.content == "no u":
        await message.channel.send("Don't no u me, you dumb **ck")
        return


    print(f'Message recieved: {message.content}')
    await message.channel.send(message.content)



client.run(TOKEN)
