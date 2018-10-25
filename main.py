import configparser
import discord
from data import Data

client = discord.Client()
data = Data()


@client.event
async def on_message(message: discord.Message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!update') and len(message.content.split(' ')) == 2:
        channel = message.channel.name
        author = message.author.name
        score = int(message.content.split(' ')[1])
        data.update(channel, author, score)
        msg = '{0.author.mention} your score has been updated to {1}:\n{2}'.format(message, score, data.leaderboard(channel))
        print('Updated {0} to {1} for {2}'.format(channel, score, author))
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!show'):
        channel = message.channel.name
        msg = 'Leaderboard for {0}:\n{1}'.format(channel, data.leaderboard(channel))
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    client.run(config['DEFAULT']['Token'])
