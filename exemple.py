import python_telegram_notification

# setup and initialize the bot
bot = python_telegram_notification.telegram_notification(add_prefix='optional_prefix_')

# send stuff
bot.send_message(bot_message='hello word')
bot.send_document(bot_document_path='exemple.py', filename='optinal_file_name.py')