# Add Telegram Notification
Easy setup of telegram notification to add to any project
with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

# Instructions
## Download
Clone this repository and put python_telegram_notification.py in your working directory
## Install requirements
    pip install -r requirements.txt

## Use the notification
Where you would like to use telegram notification add:

    import python_telegram_notification

### Initialize
The first time this code is run it will walk you through the initialization process

    bot = python_telegram_notification.telegram_notification(add_prefix='optional_prefix_')

### Send
To send notification use one of the following commands:

    bot.send_message(message_string)
    bot.send_document(PATH_TO_DOCUMENT, filename='optinal_file_name')
