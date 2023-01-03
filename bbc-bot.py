import discord
import random
import asyncio
import datetime
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Deschidere fișierul în modul de citire
with open("mesaje.json", "r") as f:
    # Încărcare conținutul fișierului într-un dictionar
    data = json.load(f)

# Accesați lista de mesaje din dictionar
messages = data["mesaje"]

# ID-ul canalului 
channel_id = 1049701964805587023

# Obține canalul folosind ID-ul său
def get_channel():
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.id == channel_id:
                return channel


async def send_random_message():
    # Așteaptă până la ora ____ zilei curente 
    now = datetime.datetime.now()
    now_today = now.replace(hour=21, minute=6, second=0, microsecond=0)
    wait_time = (now_today - now).total_seconds()
    await asyncio.sleep(wait_time)

    while True:
        # Alege un mesaj aleatoriu
        message = random.choice(messages)

        # Obține canalul
        channel = get_channel()

        # Trimite mesajul în canal
        await channel.send(message)

        # Așteaptă până la ora 23:50 a zilei următoare
        now = datetime.datetime.now()
        tomorrow_18_00 = now.replace(hour=18, minute=00, second=0, microsecond=0) + datetime.timedelta(days=1)
        wait_time = (tomorrow_18_00 - now).total_seconds()
        await asyncio.sleep(wait_time)

# Evenimentul on_ready
@client.event
async def on_ready():
    # Pornire trimiterea mesajelor
    client.loop.create_task(send_random_message())

# Rulează botul 
client.run("MTA1MjUyOTE1MDM5ODgzNjc0Ng.GwtDts.pGm7lbsFlIWx6tqp1iMH5RyYcKXD1-l2IHQgK0")
