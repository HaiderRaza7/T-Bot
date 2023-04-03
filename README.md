# T-Bot

T-Bot is a simple Discord bot that can generate random topics, topics, trivia questions, jokes, and recommendations!

## Description

This code is a Python script that defines a Discord bot that generates various types of content based on user input. The bot uses the OpenAI API to generate random topics, subtopics, trivia questions, jokes, and recommendations based on user input.

The discord and discord.ext libraries are used to create and run the bot. The openai library is used to generate the content.

The bot listens for several commands that can be triggered by users. The commands are defined using the @bot.command decorator and include:

    random-topic: generates a random topic and a brief discussion of that topic
    random-subtopic: generates three random subtopics related to a given topic
    random-trivia: generates a random trivia question related to a given topic
    random-joke: generates a random joke related to a given topic
    random-recommendation: generates three recommendations related to a given topic

Each command sends a prompt to the OpenAI API using the openai.Completion.create() method. The prompt is defined based on the user input and the type of content requested. The response from the API is used to generate the content, which is then sent to the Discord channel using the await ctx.send() method.

There is also a @bot.before_invoke decorator that logs which channels are using the bot every time a command is executed. This function is defined by the record_history function.

## Getting Started

### Dependencies

* Python packages: sys, discord, discord.ext, and openai
* Make sure you have your own discord bot created with its own token as well as your own openai API key

### Installing

* Fork this repo (Or just download main.py as that's the only file you'll need)
* If you're using an IDE like Pycharm then add your Discord bot token and openai API key as the first and second arguments to main.py, respectively

### Executing program

* Run main.py with the Discord bot token and openai API key as the arguments 
```
python main.py <bot token> <openai API key>
```

## Authors

Contributors names and contact info

[@HaiderRaza7](https://github.com/HaiderRaza7)

[//]: # (## Version History)

[//]: # ()
[//]: # (* 0.2)

[//]: # (    * Various bug fixes and optimizations)

[//]: # (    * See [commit change]&#40;&#41; or See [release history]&#40;&#41;)

[//]: # (* 0.1)

[//]: # (    * Initial Release)

## License

This project is not currently licensed.

[//]: # (This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details)

## Acknowledgments

* [ChatGPT](https://chat.openai.com/chat)
* [DomPizzie's README.md template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)