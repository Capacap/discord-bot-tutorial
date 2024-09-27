# Discord Bot Tutorial
A tutorial and example for setting up a basic Discord bot.

## Create a Discord Application
1. Go to the Discord Developer Portal and log in.
2. Click the "New Application" button and give it an appropriate name.
3. Go to the "Bot" section of your new Discord App and generate a bot token. Copy it and write it down. **Remember to keep it a secret.**
4. Scroll down a little and enable "MESSAGE CONTENT INTENT" so that your bot will be able to read messages.

## Set Up the Python Project
1. Create a folder to hold the project and give it a suitable name.
2. Open a Git Bash terminal and create a virtual environment, then activate it:
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
3. Once the environment is activated, install the required pip packages:
    ```bash
    pip install python-dotenv
    pip install discord.py
    ```
4. Create a new file named `.env`, open it, and add the following line:
    ```env
    DISCORD_BOT_TOKEN=your_bot_token_here
    ```
5. Create a Python script. Check the provided Python scripts in this repo for information on how to write the actual bot logic.

## Adding the Bot to a Server
1. On the Discord Developer Portal in your Discord Application, go to the OAuth2 section and scroll down to the OAuth2 URL Generator. It helps you generate a URL that lets you add the bot to a server.
2. In the **SCOPES** section, check the "bot" box.
3. In the **BOT PERMISSIONS** section, check the "Send Messages" and "Read Message History" boxes.
4. The resulting URL at the bottom will let you invite the bot to a Discord server. Copy the URL, then paste it into your web browser or send it to your server admin.

## Run the Bot
Run the Python script you have created. While the Python session is running, you and others can interact with your bot through Discord.

If you have not provided a shutdown command, you can still stop the bot by closing the Python terminal or by pressing `Ctrl+C` to interrupt the script.
