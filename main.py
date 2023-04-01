import sys
import discord
from discord.ext import commands
import openai


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='random-topic')
async def random_topic(ctx):
    """
    Bot generates and sends a random topic upon the command '!random-topic'.
    :param ctx: channel where the command is sent.
    """

    prompt = f'Please generate a random topic without asking it as a question and' \
             f' don\'t say anything else or even \'random topic about\''

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    topic = response.choices[0].text

    discussion_prompt = f'Please briefly discuss the following topic and' \
                        f' don\'t say anything else or even \'random topic about\': {topic}'

    discussion_response = openai.Completion.create(
        engine=model,
        prompt=discussion_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    discussion = discussion_response.choices[0].text

    await ctx.send(f'{topic}{discussion}')


@bot.command(name='random-subtopic')
async def random_sub_topic(ctx, *args):
    """
    Bot generates and sends a list of 3 random subtopics given a topic upon the command '!random-subtopic <topic>'.
    :param ctx: channel where the command was sent.
    :param args: topic to take into consideration when generating subtopics.
    """
    user_input = ' '.join(args)
    prompt = f'Please generate and list exactly 3 random subtopics about the following topic' \
             f' and don\'t say anything else or even \'random subtopic about\': {user_input}'

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    topic = response.choices[0].text
    await ctx.send(topic)
    

@bot.command(name='random-recommendation')
async def random_recommendation(ctx, *args):
    """
    Bot generates and sends a list of 3 recommendations given an example of something the user likes upon the command.
    '!random-recommmendation <something the user likes>'
    :param ctx: channel where the command was sent.
    :param args: something the user likes. The bot has to generate recommendations relevant to this.
    :return:
    """
    pass


@bot.event
async def on_ready():
    """
    Bot declares that they're online when it gets active.
    """
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
    """
    Bot announces that they're going offline shortly before doing so.
    """
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
if len(sys.argv) != 3:
    print('Correct usage: python main.py <your bot\'s token here>')
TOKEN = sys.argv[1]

openai.api_key = sys.argv[2]
model = "text-davinci-002"  # The ChatGPT model to use

bot.run(TOKEN)
