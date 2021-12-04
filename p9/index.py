import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import random
import utils
import os
import pyqrcode
import png
from pyqrcode import QRCode

TOKEN = '2103008468:AAEidIQTlQxmOturdaewnPK4YrDEnCE7L8I'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

MENU, GAME, AGE, VOICE, MAX, ARGMAX, QRCODE = range(7)


def start(update: Update, context: CallbackContext) -> int:
    text = f"{update.message.chat.username} خوش اومدی"
    update.message.reply_text(text)
    return MENU

def game(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data["rnd"] = random.randint(1,100)
    update.message.reply_text('یک عدد حدس بزن')
    return GAME

def play_game(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_reply = update.message.text
    if not utils.checkInt(user_reply):
        update.message.reply_text("عدد وارد کنید.")
        return GAME
    user_guess = int(user_reply)
    if user_guess == user_data["rnd"]:
        update.message.reply_text("آفرین درست حدس زدی")
        return MENU
    if user_guess > user_data["rnd"]:
        update.message.reply_text("پایین تر")
        return GAME
    if user_guess < user_data["rnd"]:
        update.message.reply_text("بالا تر")
        return GAME

def age(update: Update, context: CallbackContext) -> int:
    text = "سن خود را با فرمت YYYY/MM/DD وارد کنید."
    update.message.reply_text(text)
    return AGE

def response_age(update: Update, context: CallbackContext) -> int:
    user_reply = update.message.text
    try:
        age = utils.compare_date(user_reply)
    except:
        update.message.reply_text('ورودی را درست وارد نمایید')
        return AGE
    update.message.reply_text(f'سن شما: {age}')
    return MENU
    

def voice(update: Update, context: CallbackContext) -> int:
    text = "متن انگلیسی وارد کنید"
    update.message.reply_text(text)
    return VOICE

def send_voice(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    utils.text_to_speech(text)
    update.message.reply_voice(open("voice.ogg", 'rb') )
    os.remove('voice.ogg')
    return MENU


def Max(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('ارایه مورد نظر خود را وارد کنید. اعداد را با , از هم جدا کنید.')
    return MAX
def argMax(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('ارایه مورد نظر خود را وارد کنید. اعداد را با , از هم جدا کنید.')
    return ARGMAX

def max_lst(update: Update, context: CallbackContext) -> int:
    text = update.message.text

    nums = text.split(',')

    validate = [utils.checkInt(x) for x in nums]
    if not all(validate):
        update.message.reply_text('در وارد کردن اعداد دقت کنید')
        return MAX
    update.message.reply_text(f'بیشترین عدد برابر است با {max(nums)}')
    return MENU

def argmax_lst(update: Update, context: CallbackContext) -> int:
    text = update.message.text

    nums = text.split(',')

    validate = [utils.checkInt(x) for x in nums]
    if not all(validate):
        update.message.reply_text('در وارد کردن اعداد دقت کنید')
        return ARGMAX

    max_num = max(nums)
    index = nums.index(max_num)
    update.message.reply_text(f'ایندکس بیشترین عدد: {index}')
    return MENU

def qrcode(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('رشته مورد نظر خود را وارد کنید')
    return QRCODE

def qrcode_generate(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    url = pyqrcode.create(text)
    url.svg("myqr.svg", scale = 8)
    url.png('myqr.png', scale = 6)
    update.message.reply_photo(photo= open("myqr.png", 'rb'), caption="qrcode")
    return MENU

def help_bot(update: Update, context: CallbackContext) -> int:
    text = '''
    /start : خوش آمدگویی
    /game : بازی حدس اعداد
    /age : سن شما
    /voice : ارسال ویس متن شما
    /max : ماکسیسمم اعداد وارد شده
    /argmax: ایندکس بیشترین عدد
    /qrcode : تولید qrcode
    '''
    update.message.reply_text(text)
    return MENU


def main() -> None:
    """Run the bot."""
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    selection_handler = [
        CommandHandler('start', start),
        CommandHandler('game', game),
        CommandHandler('age', age),
        CommandHandler('voice', voice),
        CommandHandler('max', Max),
        CommandHandler('argmax', argMax),
        CommandHandler('qrcode', qrcode),
        CommandHandler('help', help_bot),
    ]

    conv_handler = ConversationHandler(
        entry_points= selection_handler,
        states={
            MENU: selection_handler,
            GAME:[MessageHandler(Filters.text, play_game)],
            AGE:[MessageHandler(Filters.text, response_age)],
            VOICE:[MessageHandler(Filters.regex("^[a-zA-Z0-9,.!? ]*$"), send_voice)],
            MAX:[MessageHandler(Filters.text, max_lst)],
            ARGMAX:[MessageHandler(Filters.text, argmax_lst)],
            QRCODE:[MessageHandler(Filters.text, qrcode_generate)],

        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()