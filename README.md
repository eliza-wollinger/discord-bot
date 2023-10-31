# Pepper - The Motivational Discord Bot

Pepper is an uplifting bot designed to identify words that express sadness in another person and respond with words of encouragement. 😁

## How to Interact with Pepper

1. Start by saying ``Hello``. 👋
1. If you're feeling sad, express your emotions by saying words like ``Unhappy``, ``Sad`` or ``Angry``, and Pepper will provide motivational responses. 🔼
1. If you're in need of an inspiring message, simply say  ``Inspire me``. ✨

---

### Running the Bot

Due to security considerations, the bot's private key cannot be included in the code. To make Pepper work, you need to replace the 'TOKEN' in the code with your own bot token.

You can run the bot using the following commands in your terminal:

On Windows:
```sh
py -3 main.py
```

On other systems:
```sh
python3 main.py
```

---

### Development Details ⚙️

Pepper was developed using the discord.py library. Here's a brief overview of how it works:

- An instance of the user, as a Client, is created to connect the code with Discord.
- The decorator ```@client.event()``` is used to register events. Since this is an asynchronous library, events are handled through callbacks. Callbacks are functions that are called when certain events occur.
- The ```on_ready()``` event is triggered when the bot is ready to be used. When the bot receives a message, the ```on_message()``` event is called.
- To generate random inspirational quotes, the ```get_quote()``` function is defined. It uses the requests module to retrieve data from the Zen Quotes API.

Pepper is here to spread positivity and encouragement in your Discord conversations! 😊🌟
