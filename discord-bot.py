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
        print(response.text)

        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_BOT_ID)
