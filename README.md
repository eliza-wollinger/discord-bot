![Discord Bot Banner](https://user-images.githubusercontent.com/57842220/127756437-a8f1f97d-d323-4fd1-b48c-39dfdbf7d067.png)

Pepper is a motivational bot that identifies words that characterize another person's sadness and responds with something **encouraging**... 😁

To develop it I used the ```discord.py``` library, with it I created an instance of our user, as a ```Client```. What connects the code with Discord.

After I used the decorator ```@client.event()``` to register an event. This is an asynchronous library, so things are done with callbacks. A callback is a function that is called when something else happens.
> In this code, the ```on_ready()``` event is called when the bot is ready to start being used. So when the bot receives a message, the ```on_message()``` event is called.

To generate the random inspirational quotes, I defined the ```get_quote()``` function. First, it uses the requests module to request data from the Zen Quotes API URL.

---

### How to Run the Bot? 🏃‍♀️

Due to security concerns, the bot's private key cannot be in the code, so to work, you need to replace the **TOKEN** in ```client.run('TOKEN')```.

You can use these commands in the terminal to run the bot:

On Windows:
```py -3 main.py```

On other systems:
```python3 main.py```
