import python_telegram_notification

# setup and initialize the bot
bot = python_telegram_notification.telegram_notification()

# send stuff
bot.send_message('hello word')
bot.send_document('README.md')
