import discord
import asyncio
from responses import *

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def lua_to_json(lua):
    return 'hello'

@client.event
@asyncio.coroutine
def on_message(message):
    rep = text = msg = message.content
    rep2 = text2 = msg2 = rep.split()
    user = str(message.author)
    user_bot_client = client.user.name
    try:
        command = rep2[0].lower()
    except IndexError:
        command = ""

    print('help fr' in responses)

    print(message.author)
    if message.channel.is_private and message.author.id != client.user.id:
        if rep in responses:
            yield from client.send_message(message.channel,responses.get(rep))
        else:
            yield from client.send_message(message.channel,responses.get('help'))

client.run('my discord key')

