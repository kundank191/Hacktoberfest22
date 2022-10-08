# Send Automated Message in telegram Channel

Generic Function to send message to telegram channel

# Setup

## Telegram Setup

### Step 1 : Create A bot
- Search For Bot Father in Telegram
- type `/newbot` and follow process to create a bot
- Store the Bot API token

### Step 2 : Get the channel/group/chat where you want the bot to sent the message
- Add bot @getmyid (IDbot) to the channel
- type `/getgroupid` To get the group id
- Store the group id

### Step 3 : Add the bot to the Channel/grouo
- Add the bot as an admin to the channel

## Project Setup
- create a new file inside folder secret called `secret_keys.py`
- add your secret keys in the variable `TELEGRAM_BOT_API_KEY`
- Use the function `send_message_to_chat` to send message to telegram


