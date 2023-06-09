import sys
import discord
from discord.ext import commands
import openai


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.before_invoke
async def record_history(ctx):
    """
    Logs which channels are using the bot everytime a command is executed.
    :param ctx: Context object.
    """
    print(f'A command was triggered in channel name {ctx.channel} with id {ctx.channel.id}!')


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


@bot.command(name='random-trivia')
async def random_trivia(ctx, *args):
    """
    Bot generates and sends a random trivia question based on the given topic upon the command '!random-trivia <topic>'
    :param ctx: channel where the command was sent.
    :param args: topic to take into consideration when generating the trivia question.
    """
    user_input = ' '.join(args)
    prompt = f'Please generate a random trivia question relevant to the following topic' \
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


@bot.command(name='random-joke')
async def random_joke(ctx, *args):
    """
    Bot generates and sends a random joke based on the given topic upon the command '!random-joke <topic>'
    :param ctx: channel where the command was sent.
    :param args: topic to take into consideration when generating the joke.
    """
    user_input = ' '.join(args)
    prompt = f'Please generate a random joke relevant to the following topic' \
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
    user_input = ' '.join(args)
    prompt = f'Please list the type of entertainment media or game'\
             f' the following is most enjoyed in and nothing else at all:{user_input}. Your answer should usually be' \
             f' 1 word. Your answer must be less than 4 words in total.'

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    medium = response.choices[0].text

    prompt = f'Please generate a {medium} recommendation relevant to the following {medium} that isn\'t what I am ' \
             f'about to say and don\'t say anything else or even \'random subtopic about\': {user_input}'

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
                    print(f'Bot is now active in channel {channel.id}!')
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
