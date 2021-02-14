"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Deployed using heroku.
"""

import logging

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import secrets
from PIL import Image
import random
import string


def get_random_alphanumeric_string(length):
    """ Get a string of random alphanumeric characters of specified length"""
    return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(length)))


TOKEN = os.environ['ENV_BOT_TOKEN']
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

start_text = """
Author: [incend1ary](https://t.me/incend1ary) \[Aleksei Seliverstov\]
Source code: [GitHub](https://github.com/1ncend1ary/ams_test_task)

/start \- display this message
/help \- get commands help
/coords lat long \- get a map with marked location
Format: 0 <\= lat <\= 100, 0 <\= long <\= 100
"""

commands_text = """
/start \- display the start message
/help \- get this help
/coords lat long \- get a map with marked location
Format: 0 <\= lat <\= 100, 0 <\= long <\= 100
"""


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(start_text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(commands_text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def coords(update, context):
    """Send the coordinates picture"""
    try:
        long, latt = map(float, update.message.text.split()[1:])
    except ValueError:
        update.message.reply_text('Incorrect coordinates specified')
        return

    img = Image.open('res/loc.png', 'r')
    img = img.convert('RGBA')
    img = img.resize((16, 16))
    img_w, img_h = img.size
    background = Image.open('res/Trad_trasses.jpg', 'r')
    bg_w, bg_h = background.size
    offset = (0, 0)
    background.paste(img, offset, img)  # third parameter is alpha mask
    filename = get_random_alphanumeric_string(12)
    background.save(f'res/{filename}.png')
    update.message.reply_photo(photo=open(f'res/{filename}.png', 'rb'))
    os.remove(f'res/{filename}.png')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("coords", coords))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    # Use updater instead of poller
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://ams-test-task.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
