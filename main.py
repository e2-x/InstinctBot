import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def example_func(author,message):
    client.send_message(message.channel,"%s, How are you?" % author)


@client.event
async def on_message(message):
    author = message.author
    if message.content.startswith('!test'):
        example_func(author,message)

client.accept_invite('https://discord.gg/z44bM')
client.run('MjA1MDE0MzUxMzM2MTc3NjY0.Cm_1_g.v3iRnRZ908AMQPNLIS-HR6B9Nzk')