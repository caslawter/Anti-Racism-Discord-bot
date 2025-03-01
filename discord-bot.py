# This example requires the 'message_content' intent.

import discord
from flask import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_ID = os.getenv('DISCORD_BOT_ID')
MODEL_SERVER_IP = os.getenv('MODEL_SERVER_IP')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


    async def on_message(self, message):
        url = f'{MODEL_SERVER_IP}/check'
        data = {'sentence': message.content}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        data = json.loads(response.text)
        print(data)
        if(data['is_racist'] and data['score'] > 0.85):
            await message.delete()
            await message.channel.send(f'Hi there {message.author}. Can you stop being racist?')

        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_BOT_ID)
