# Import from built-in os package
from os import getenv
# Import from python-dotenv package
from dotenv import load_dotenv
# Import from discord package
from discord import Message, Intents
from discord.ext.commands import Bot

# This class contains all data relating to the discord bot
class DiscordBotContainer:
    # Initialize the bot container by providing a Discord Bot Token
    def __init__(self, bot_token: str) -> None:
        # The bot token functions like a password that gives your bot access to discord services
        # It is similar to an API key
        self.bot_token = bot_token

        # Example data attribute we will use with the bot
        self.python_mention_count = 0

    def run_bot(self) -> None:
        # The bot needs to have defined 'intents' which announces to the server what type of data the bot needs access to
        intents = Intents.default()
        intents.message_content = True # You need to enable "MESSAGE CONTENT INTENT" on the Bot section of your Discord App on Discord Developer Portal to be able to work with messages

        # Create an instance of a discord bot
        # command_prefix is the symbol that proceeds commands triggerd by functions with the @bot.command decorator
        bot = Bot(command_prefix="!", intents=intents, case_insensitive=True)

        # Below are functions that will be attached to the bot decoratd with @bot.event and @bot.command
        # all bot functions must be async functions

        # This function will trigger when the bot first becomes ready to send and recieve messages
        # The @bot.event decorator marks bot functions that are not commands
        @bot.event
        async def on_ready():
            print(f"{bot.user} is ready")

        # This function will trigger everytime the bot reads a message
        # The message argument is the discord message the bot read, it contains data such as who wrote it and what channel it was posted in
        @bot.event
        async def on_message(message: Message):
            # Here we ensure the bot does not read its own messages
            if message.author == bot.user:
                return
            
            # In the on_message function we can process and do things with messages even if they are not commands
            if "python" in message.content.lower():
                self.python_mention_count += 1
            
            # This will trigger make the message trigger a command if one exists
            bot.process_commands(message)

        #The @bot.command decorator marks this function as a command
        # Users can trigger it by writing the command prefix followed by the name of the function, eg. "!greet"
        @bot.command
        async def greet(message: Message):
            # Send a message on the same channel the command was posted on
            await message.channel.send(f"Greetings {message.author.display_name}!")

        # Here is a simple command that uses data stored in the DiscordBotContainer object
        @bot.command
        async def greet(message: Message):
            await message.channel.send(f"Python has been mentioned {self.python_mention_count} times.")

        # This is a command that can only be triggered by the bot's owner
        @bot.command
        async def shutdown(message: Message):
            owner = bot.is_owner(message.author)
            if await owner:
                await message.channel.send("Shutting down...")
                # This will shutdown the bot
                await bot.close()

        # Once all commands have been defined use this to start the bot
        bot.run(self.bot_token)


if __name__ == "__main__":
    # Load the dotenv
    load_dotenv()
    # get the discord bot token from the .env
    bot_token = getenv("DISCORD_BOT_TOKEN")
    # Create an instance of DiscordBotContainer
    discord_bot = DiscordBotContainer(bot_token)
    # Tell the DiscordBotContainer to instantiate the bot
    discord_bot.run_bot()