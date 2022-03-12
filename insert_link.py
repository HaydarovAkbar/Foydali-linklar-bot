from telegram.ext import CallbackContext
from telegram import Update
from connect import Database
from battons import about,all_category_by_link
from datetime import datetime

database = Database()
bot_data = {}

def get_insert_full_link(update:Update, context:CallbackContext):
    update.message.reply_html("<code>Link kategoriyasini tanlang</code>",
                              reply_markup=all_category_by_link())
    return 50
    # photo = update.message.photo[0]["file_id"]

def get_category_by_link(update:Update, context:CallbackContext):
    global bot_data
    chat_id = update.effective_chat.id
    query = update.callback_query
    bot_data[chat_id] = query.data
    query.delete_message(timeout=0.5)
    context.bot.send_message(chat_id=chat_id,text = "<code>Siz Tayyor link bo'limidasiz.\n"
                              "Endi siz Linkni butunligicha kiritishingiz mumkin!\n"
                              "Ichida '$' belgi bo'lmasligiga etibor bering</code>",
                             parse_mode = 'HTML',
                             reply_markup=about)
    return 51

def insert_full_link(update:Update, context:CallbackContext):
    photo = update.message.photo[0]['file_id']
    chat_id = update.effective_chat.id
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    discription = update.message.caption
    name, text, link = discription.split('$')
    A = database.set_link(text,photo,link,chat_id,now,name,bot_data[chat_id])
    print(A)
    return 2
