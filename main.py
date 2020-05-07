import telegram, os, requests, datetime, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# https://stackoverflow.com/questions/48364204/sending-voice-command-to-telegram-bot

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# tokens and api keys
TOKEN = "1143363333:AAFuxEZNNbGxuBeBGqH37x9U-mJGomD-XLw"

bot = telegram.Bot(token=TOKEN)
up = Updater(token=TOKEN, use_context=True)
dp = up.dispatcher

def start(update, context):

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="FooBar",
        parse_mode=telegram.ParseMode.MARKDOWN
    )

def cb(update, context):
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Thanks for the message"
    )

audio_handler = MessageHandler(
    Filters.all,
    cb
)



dp.add_handler(CommandHandler('start', start))
dp.add_handler(audio_handler)

up.start_polling()
up.idle()