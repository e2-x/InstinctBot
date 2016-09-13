import discord
import requests
import json

client = discord.Client()
botCommands = {}


async def get_poke_url(message):
    poke_name = message.strip('!')
    pokeNumUrl = 'http://pokeapi.co/api/v2/pokemon/'
    req = requests.get(pokeNumUrl)
    data = req.text
    parsedData = json.loads(data)
    for key, value in parsedData.items():
        #print(key ,' < Keys: Values ->',value)
        if 'results' in key:
            #print(value[0]['url'])
            if poke_name in value[0]['name']:
                print(value[0]['url'])

async def respond_in_tChannel(author, message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, "%s, How are you?" % author)
    elif "instinct" in message.content:
        await client.send_message(message.channel, ":zap: TEAM INSTINCT :zap:")
    elif "valor" in message.content:
        await client.send_message(message.channel, "https://img.memecdn.com/go-team-mystic_c_6826207.jpg")

async def summon_bot(vchannel, tchannel):
    await client.send_message(tchannel, 'has joined %s successfully!:alien:' % vchannel)
    await client.join_voice_channel(vchannel)


@client.event
async def on_message(message):
    author = message.author
    mess = message.content
    voiceChannel = message.author.voice_channel
    textChannel = message.channel
    #print(pokeList)
    #-----------------------------------------#
    await respond_in_tChannel(author, message)
    #await return_json()

    if mess.startswith('!summon'):
        if author.server.owner.voice_channel != author.server.me.voice_channel:
            await summon_bot(voiceChannel, textChannel)
        else:
            await client.send_message(textChannel, 'I am already in here senpai!')
    else:
        await get_poke_url(mess)

    # if mess in get_poke_url().pokeNumUrl:
    #     print(get_poke_url().pokeNumUrl[mess])
    #     await client.send_message(message.channel, 'http://pokeapi.co/media/sprites/pokemon/'+ str(get_poke_url().pokeNumUrl[mess]) + '.png \n Type: Grass \n Small')


client.accept_invite('https://discord.gg/ASqwh')
client.run('MjA1MDE0MzUxMzM2MTc3NjY0.CnBejQ.IXZ8QIiO1TKrCVnOlaMf40hQJ2E')

