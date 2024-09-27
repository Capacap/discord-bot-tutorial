# discord-bot-tutorial
A tutorial and example for setting up a basic discord bot

Create a Discord Application
    Go to the discord developer portal at https://discord.com/developers and log in. Click the "New Application" button and give it an apropriate name. Go to the "Bot" section of yur new Discord App and generate a bot token, copy it and write it down. Remember to keep it a secret.
    Scroll down a little and enable "MESSAGE CONTENT INTENT" so that your bot will be able to read bessages.

Set Up the Python Project
    Create a folder to hold the project and give it a suitable name. Open a git bash terminal and create a virtual environment and activate it.
    python -m venv venv
    source venv/Scripts/activate
    Once the environment is activated install the required pip packages.
    pip install python-dotenv
    pip install discord.py
    Once installed, create a new file and name it ".env", open it and add the line DISCORD_BOT_TOKEN = your-token-goes-here. Create a python script, check the provided python scripts in this repo for information on how to write the actual bot logic.

Adding the Bot to a Server 
    On the Discord Developer Portal in your Discord Application, go to the OAuth2 section and scroll down to the OAuth2 URL Generator. It helpss you generate a URL that lets you add the bot to a server. In the SCOPES section check "bot" box then in the BOT PERMISSIONS section check "Send Messages" and "Read Message History" boxes. The resulting URL at the bottom will let you invite the bot to a discord server. Copy the URL then paste it into your web browser or send it to your server admin.

Run the bot:
    Run the python script you have created, while the python session is running you and others can interact with your bot though discord. If you have not provided a shutdown comman, you can still stop the bot by closing the python terminal or by pressing ctrl-C to interrupt the script.