import datetime
import inspect
import os

import discord

import commands
from responses import responses


# Create a class of the bot
class LGBot(discord.Client):

    # Initialization when class is called
    def __init__(self):
        # Set intents for the bot
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.synced = False
        self.added = False

    # Wait until bot is ready
    async def on_ready(self):
        # Waits until internal cache is ready
        await self.wait_until_ready()

        # Import commands and sync
        command_tree = discord.app_commands.CommandTree(self)
        commands.commands_list(self, command_tree)
        if not self.synced:
            await command_tree.sync()
            self.synced = True
        if not self.added:
            self.added = True

        # Set activity of the bot
        activity = discord.Activity(type=discord.ActivityType.listening, name="Les ordres de Flens")
        await self.change_presence(activity=activity, status=discord.Status.online)

        # Check the number of servers the bot is a part of
        print(f"Number of servers I'm in : {len(self.guilds)}")

        # Prints in the console that the bot is ready
        print(f'{self.user} is now online and ready!')

    # Event when the bot receives a message
    async def on_message(self, message):
        # If the message is from a bot, ignore
        if message.author.bot:
            return

        # Stock the message's information in variables
        username = str(message.author)
        user_msg = str(message.content)
        channel = message.channel

        # Call responses with message of the user and responds if necessary
        response = await responses(self, user_msg, channel)
        if not response == '':
            await channel.send(response)
            print(f'{self.user} responded : "{response}" to {username}')

    async def on_typing(self, channel, user, when: datetime.datetime):
        if when.month == 4 and when.day == 1:
            await channel.send(f"{user.mention} tape plus vite ton message")


# Function to run the bot
def run_bot():
    # Import token from file
    module_path = inspect.getfile(inspect.currentframe())
    module_dir = os.path.realpath(os.path.dirname(module_path))
    with open(f"{module_dir}/token", "r") as file:
        token = file.read()

    # Create an instance of the LGBot class
    client = LGBot()

    # Run the client with the token
    client.run(token, reconnect=True)