import os
import json
import random
import discord
import requests

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person/bot!"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('Hello'):
    await message.channel.send('Hello human! How are you?')

  if msg.startswith('Inspire me'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run('ODcxMTMxOTMyMTgyODY4MDU4.YQW21Q.WnSPcoBTHfcRiud2rQcD-Le1u0E')