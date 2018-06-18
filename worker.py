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
    yield from client.change_presence(game=discord.Game(type=0, name='Dofucks ♥'))


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

    # print('help fr' in responses)
    i = client.get_all_emojis()
    if 'soso' in message.content.lower():
        yield from client.add_reaction(message, ':soso:455704568937054209')

    if client.user.mentioned_in(message) and len(message.mentions) == 1:
        yield from client.send_message(message.channel, "Je ne suis pas disponible pour le moment. Je pratique une expérience sur des @Lab Rat , envoie moi un message privé !")
    if message.channel.is_private and message.author.id != client.user.id:
        print(message.author)
        print(message.content)
        if rep in responses:
            yield from client.send_message(message.channel, responses.get(rep))
        else:
            yield from client.send_message(message.channel, responses.get('help'))


@client.event
@asyncio.coroutine
def on_member_join(member):
    yield from client.send_message(member, """
:flag_fr: 
Bienvenue sur notre Discord """ + member.name + """ !
Pour profiter pleinement de Dofucks et faire partie intégrante de notre communauté, accéder aux scripts partagés ou apprendre à utiliser l'outil, n'hésitez pas à vous rendre sur notre forum et à vous inscrire : https://forum.dofucks.com/
Vous pouvez aussi me poser des questions, pour savoir comment, envoyez moi un message ici.

:flag_us: 
Welcome to our Discord """ + member.name + """ !
To take full advantage of Dofucks and be an integral part of our community, access shared scripts or learn how to use the tool, feel free to visit our forum and register: https://forum.dofucks.com/
You can also ask me questions, to know how, send me a message here.""")


client.run('')

