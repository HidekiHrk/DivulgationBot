import discord
import json

with open('./config.json', 'r') as f:
    config = json.load(f)

with open('./messages.txt', 'r') as f:
    rd = f.read()
    messages = [x.strip() for x in rd.split('-=-=-end-=-=-')]

def msgs(strings):
    snum = 0
    while True:
        if snum >= len(strings):
            snum = 0
        yield strings[snum]
        snum += 1
msgs = msgs(messages)
del messages


with open('./blacklist.txt', 'r') as f:
    rd = f.read()
    blacklist = list(map(lambda x: int(x), rd.split('\n'))) if rd else []

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print('-'*30)
    print('Nome:', client.user.name)
    print('ID:', client.user.id)
    print('-'*30)

@client.event
async def on_message(msg):
    if msg.author.bot: return
    if msg.content.startswith('div') and msg.author.id in config['adms']:
        guild = await client.fetch_guild(config['server_id'])
        await msg.channel.send(f'{msg.author.mention}, divulgando para os membros da guild: ``{guild.name}``')
        async for member in guild.fetch_members(limit=None):
            if member.id in blacklist: continue
            print('-'*30)
            print(f'divulgando para {member}')
            try:
                await member.send(next(msgs))
                print('feito')
            except Exception as e:
                print('erro:', e)
            finally:
                print('-'*30)

        print('completo')
        await msg.channel.send(f'{msg.author.mention}, Feito!')

client.run(config['token'])