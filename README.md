Welcome to this workshop! We're going to build a Discord bot with [discord.py](https://discordpy.readthedocs.io/en/latest/) and Python. Let's dive right into it!

# Build a Discord Bot

## Prerequisites

- Python and Pip
- A Discord account

## Step 1: Create a Bot Account

1.  Make sure you’re logged on to the [Discord website](https://discord.com/).

2.  Navigate to the [application page](https://discord.com/developers/applications)

3.  Click on the “New Application” button.

    ![The new application button.](https://discordpy.readthedocs.io/en/v1.3.3/_images/discord_create_app_button.png)

4.  Give the application a name and click “Create”.

    ![The new application form filled in.](https://discordpy.readthedocs.io/en/v1.3.3/_images/discord_create_app_form.png)

5.  Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”.

    ![The Add Bot button.](https://discordpy.readthedocs.io/en/v1.3.3/_images/discord_create_bot_user.png)

    - Click “Yes, do it!” to continue.

6.  If you want others to invite your bot, make sure that **Public Bot** is ticked. Also, make sure that **Require OAuth2 Code Grant** is unchecked.

    ![How the Bot User options should look like for most people.](https://discordpy.readthedocs.io/en/v1.3.3/_images/discord_bot_user_options.png)

7.  Copy the token using the “Copy” button.

    - **NOTE: This is not the same thing as the Client Secret on the General Information page**
    - **WARNING: This token is equivalent to your bot's password, so do not share it with anyone.**

## Step 2: Invite Your Bot

1.  Go to the “OAuth2” tab

    ![How the OAuth2 page should look like.](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2.png)

2.  Tick the “bot” checkbox under “scopes”

    ![The scopes checkbox with "bot" ticked.](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_scope.png)

3.  Tick the permissions required for your bot to function under “Bot Permissions”

    ![The permission checkboxes with some permissions checked.](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_perms.png)

4.  Now the resulting URL can be used to add your bot to a server. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.

Source: [https://discordpy.readthedocs.io/en/latest/discord.html](https://discordpy.readthedocs.io/en/latest/discord.html)

## Step 3: Setup Your Environment

1. Install or upgrade discord.py: `python -m pip install discord.py`
	- NOTE: you may need to use a variation of the pip command depending on your platform.
2. Create a new file called `.env` that is a copy of the contents of `.env-example`.
3. Replace `placeholder_token` within the `.env` with your token that you can acquire from part 7 of step 1. Do not share this token with anyone, it's your bot's password.

### Step 4: Program your bot!

Examples of what you can do with a basic bot can be found in the `main.py` file.
