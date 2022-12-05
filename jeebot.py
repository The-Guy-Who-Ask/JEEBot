from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from requests import *
from telegram import *
from datetime import datetime as dt

randomPImageUrl = "https://picsum.photos/1200"

date_format = "%m/%d/%Y"
jeedat = dt(2023,1,26)

updater = Updater("5836658304:AAEiWmnORjOiY76ee5lYKe4CgeZG6pX4eL4",
				use_context=True)

def start(update: Update, context: CallbackContext):
   update.message.reply_text("Hello dear ol jeetards")
  
def Timer(update: Update, context: CallbackContext):
	today=dt.today()
	djeedat = dt.strftime(today,'%m/%d/%Y')
	fdat =  dt.strptime(djeedat, date_format)
	leday = jeedat-fdat

	image = get(randomPImageUrl).content
	context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption="Days To JEE 2023 : {}".format(leday.days))])

def studytime(update: Update, context: CallbackContext):
	now = dt.now()
	current_time = now.strftime("%H:%M:%S")
	update.message.reply_text("Study Timer Started : {}".format(current_time))
	

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('timer', Timer))
updater.dispatcher.add_handler(CommandHandler('study', studytime))

updater.start_polling()
