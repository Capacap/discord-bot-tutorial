from os import getenv
from dotenv import load_dotenv
from discord import Message, Intents
from discord.ext.commands import Bot

class discord_bot_container:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def main(self) -> None:

        intents = Intents.default()
        intents.message_content = True

        bot = Bot(command_prefix="!", intents=intents, case_insensitive=True)

        @bot.event
        async def on_ready():
            print(f"{bot.user} is ready")

        @bot.event
        async def on_message(message: Message):
            if message.author == bot.user:
                return

            if message.content.startswith("!greet"):
                await message.channel.send(f"Greetings {message.author.display_name}!")

            if message.content.startswith("!shutdown"):
                owner = bot.is_owner(message.author)
                if await owner:
                    await message.channel.send("Shutting down...")
                    await bot.close()

        bot.run(self.api_key)

if __name__ == "__main__":
    load_dotenv()
    api_key = getenv("DISCORD_BOT_TOKEN")
    discord_bot = discord_bot_container(api_key)
    discord_bot.main()