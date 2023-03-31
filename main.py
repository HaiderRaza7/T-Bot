import sys
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='random-topic')
async def rtopic(ctx):
    topic = 'insert random topic here'  # THIS SHOULD BE A RANDOM TOPIC FROM CHATGPT
    await ctx.send(topic)


@bot.command(name='random-sub-topic')
async def rtopic(ctx):
    topic = 'insert random topic here'  # THIS SHOULD BE A RANDOM TOPIC FROM CHATGPT
    await ctx.send(topic)


@bot.event
async def on_ready():
    # Loop through all servers the bot is in
    for guild in bot.guilds:
        # Loop through all channels in each server
        for channel in guild.text_channels:
            # Check if the channel is a TextChannel (as opposed to a VoiceChannel or CategoryChannel)
            if channel.name == 'general':
                try:
                    # Send a message to the channel
                    await channel.send("I'm online!")
                except discord.errors.Forbidden:
                    # If the bot does not have permission to send messages in the channel, catch the exception
                    pass


@bot.event
async def on_disconnect():
    # Loop through all servers the bot is on
    for guild in bot.guilds:
        # Loop through all channels in each server
        for channel in guild.text_channels:
            if channel.name == 'general':
                try:
                    await channel.send("I'm going offline now, see you later!")
                except Exception as e:
                    print(f"Couldn't send message to {channel.name} in {guild.name}: {e}")


# rTopic Bot's token
# noinspection SpellCheckingInspection
if len(sys.argv) != 2:
    print('Correct usage: python main.py <your bot\'s token here>')
TOKEN = sys.argv[1]
bot.run(TOKEN)
