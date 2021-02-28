"""
Simple Bot taken from the python-telegram-bot examples.
Deployed using heroku.
"""

import logging
import os
import random
import string

import telegram
from PIL import Image
from telegram.ext import Updater, CommandHandler

import secrets
import static


def get_random_alphanumeric_string(length):
    """ Get a string of random alphanumeric characters of specified length"""
    return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(length)))


TOKEN = os.environ['ENV_BOT_TOKEN']
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(static.start_text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def help_nandler(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(static.commands_text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def coords(update, context):
    """Send the coordinates picture"""
    try:
        y, x = map(float, update.message.text.split()[1:])
        if y < static.min_h or x < static.min_w or y > static.max_h or x > static.max_w:
            raise ValueError
    except ValueError:
        update.message.reply_text('Incorrect coordinates specified')
        return

    background = Image.open('res/map.jpg', 'r')
    bg_w, bg_h = background.size
    fg_size = int(min(bg_w, bg_h) * 7 / 100)
    foreground = Image.open('res/loc.png', 'r').convert('RGBA').resize((fg_size, fg_size))

    offset = (int((x - static.min_w) / (static.max_w - static.min_w) * bg_w - fg_size / 2),
              int(bg_h - (y - static.min_h) / (static.max_h - static.min_h) * bg_h - fg_size))
    background.paste(foreground, offset, foreground)  # third parameter is alpha mask

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
    dp.add_handler(CommandHandler("help", help_nandler))
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
