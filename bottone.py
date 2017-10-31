import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
import datetime
import time
import logging
from addone import add_one

#check the updates https://api.telegram.org/bot491260950:AAFIioB9Drkaa22AM5YhHP8oEtuUZJN5Z5M/getUpdates

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

token = "491260950:AAFIioB9Drkaa22AM5YhHP8oEtuUZJN5Z5M"

#poet bot will echo the previous message whatever the message from the user is
def echone(bot, update):

    name = str(update.message.chat.first_name).split(" ")
    message = str(update.message.text).split(" ")

    name = [add_one(x) for x in name]
    name = " ".join(name) 

    message = [add_one(x) for x in message]
    message = " ".join(message)

    t = ("%s " + message + " eccome!") % name
    bot.send_message(chat_id=update.message.chat_id, text=t)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(token=token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echone))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
