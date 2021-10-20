from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from methods import *
from battons import *

updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

all_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  CallbackQueryHandler(inline_funcion),
                  MessageHandler(Filters.regex('^(' + web + ')$'), battons1),
                  MessageHandler(Filters.regex('^(' + kanal + ')$'), battons2),
                  MessageHandler(Filters.regex('^(' + bot + ')$'), battons3),
                  MessageHandler(Filters.regex('^(' + boshqa + ')$'), battons4),
                  MessageHandler(Filters.regex('^(' + haqida + ')$'), battons5),
                  MessageHandler(Filters.regex('^(' + add + ')$'), battons6),
                  MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
                  MessageHandler(Filters.regex('^(' + "Delete link" + ')$'), link_delete),
                  MessageHandler(Filters.regex('^(' + "Add link" + ')$'), add_link),
                  MessageHandler(Filters.regex('^(' + "Add reklama" + ')$'), reklama),
                  MessageHandler(Filters.regex('^(' + "Add admin" + ')$'), add_admin),
                  MessageHandler(Filters.regex('^(' + "Admins" + ')$'), admin_lists),
                  MessageHandler(Filters.regex('^(' + "Users" + ')$'), all_user),
                  ],
    states={
        1: [
            CommandHandler('start', start),
            CallbackQueryHandler(inline_funcion),
            MessageHandler(Filters.regex('^(' + web + ')$'), battons1),
            MessageHandler(Filters.regex('^(' + kanal + ')$'), battons2),
            MessageHandler(Filters.regex('^(' + bot + ')$'), battons3),
            MessageHandler(Filters.regex('^(' + boshqa + ')$'), battons4),
            MessageHandler(Filters.regex('^(' + haqida + ')$'), battons5),
            MessageHandler(Filters.regex('^(' + add + ')$'), battons6),
            MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.regex('^(' + "Delete link" + ')$'), link_delete),
            MessageHandler(Filters.regex('^(' + "Add link" + ')$'), add_link),
            MessageHandler(Filters.regex('^(' + "Add reklama" + ')$'), reklama),
            MessageHandler(Filters.regex('^(' + "Add admin" + ')$'), add_admin),
            MessageHandler(Filters.regex('^(' + "Admins" + ')$'), admin_lists),
            MessageHandler(Filters.regex('^(' + "Users" + ')$'), all_user),
        ],
        # bu Admin yoki user qushish funskiyasiga kirganda ishlidigan methodlar!
        2: [MessageHandler(Filters.regex('^(' + "🌏WebSayt qo'shish" + ')$'), category_web),
            MessageHandler(Filters.regex('^(' + "🌏Kanal qo'shish" + ')$'), category_channel),
            MessageHandler(Filters.regex('^(' + "🌏Bot qo'shish" + ')$'), category_bot),
            MessageHandler(Filters.regex('^(' + "🌏Boshqa link" + ')$'), category_boshqa),
            MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.regex('^(' + "Delete link" + ')$'), add_delete_linkID),
            MessageHandler(Filters.regex('^(' + "Add link" + ')$'), add_link),
            MessageHandler(Filters.regex('^(' + "Add reklama" + ')$'), reklama),
            MessageHandler(Filters.regex('^(' + "Add admin" + ')$'), add_admin),
            MessageHandler(Filters.regex('^(' + "Admins" + ')$'), admin_lists),
            MessageHandler(Filters.regex('^(' + "Users" + ')$'), all_user),
            ],
        3: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, name_func)],
        4: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, text_func)],
        5: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, link_func)],
        6: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.photo, photo_func)],
        7: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, link_delete)],
        9: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, get_new_admin_name)],
        10: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
             MessageHandler(Filters.text, get_new_adminID)],
        11: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
             MessageHandler(Filters.text, get_new_admin_username)],
        8: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
            MessageHandler(Filters.text, rek)],
        12: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
             MessageHandler(Filters.regex('^(' + "📝 Text" + ')$'), rek_text1),
             MessageHandler(Filters.regex('^(' + "🎥 Video" + ')$'), rek_Video1),
             MessageHandler(Filters.regex('^(' + "🏞 Photo" + ')$'), rek_photo1),
             ],
        13: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
             MessageHandler(Filters.photo, rek_photo)],
        14: [MessageHandler(Filters.regex('^(' + "Menyu" + ')$'), start),
             MessageHandler(Filters.video, rek_video)],
    },
    fallbacks=[MessageHandler(Filters.text, fallback_text)]
)

dispatcher.add_handler(all_handler)

updater.start_polling()
print("Bot ishladi")
