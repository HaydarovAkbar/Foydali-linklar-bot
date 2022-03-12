from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from methods import *
from battons import *
from insert_link import *

updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

all_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  CommandHandler('developer', developer),
                  CallbackQueryHandler(inline_funcion),
                  MessageHandler(Filters.regex('^(' + web + ')$'), battons1),
                  MessageHandler(Filters.regex('^(' + kanal + ')$'), battons2),
                  MessageHandler(Filters.regex('^(' + bot + ')$'), battons3),
                  MessageHandler(Filters.regex('^(' + boshqa + ')$'), battons4),
                  MessageHandler(Filters.regex('^(' + haqida + ')$'), battons5),
                  MessageHandler(Filters.regex('^(' + add + ')$'), battons6),
                  ],
    states={
        1: [
            CommandHandler('start', start),
            CommandHandler('developer', developer),
            CallbackQueryHandler(inline_funcion),
            MessageHandler(Filters.regex('^(' + web + ')$'), battons1),
            MessageHandler(Filters.regex('^(' + kanal + ')$'), battons2),
            MessageHandler(Filters.regex('^(' + bot + ')$'), battons3),
            MessageHandler(Filters.regex('^(' + boshqa + ')$'), battons4),
            MessageHandler(Filters.regex('^(' + haqida + ')$'), battons5),
            MessageHandler(Filters.regex('^(' + add + ')$'), battons6),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.regex('^(' + full_join_link + ')$'), get_insert_full_link),
        ],
        # bu Admin yoki user qushish funskiyasiga kirganda ishlidigan methodlar!
        2: [CommandHandler('start', start),
            CommandHandler('developer', developer),
            MessageHandler(Filters.regex('^(' + add_web_sayt + ')$'), category_web),
            MessageHandler(Filters.regex('^(' + add_channel + ')$'), category_channel),
            MessageHandler(Filters.regex('^(' + add_bot + ')$'), category_bot),
            MessageHandler(Filters.regex('^(' + add_other_link + ')$'), category_boshqa),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.regex('^(' + del_link + ')$'), add_delete_linkID),
            MessageHandler(Filters.regex('^(' + full_join_link + ')$'), get_insert_full_link),
            MessageHandler(Filters.regex('^(' + add_link_txt + ')$'), add_link),
            MessageHandler(Filters.regex('^(' + add_rek + ')$'), reklama),
            MessageHandler(Filters.regex('^(' + add_admin_txt + ')$'), add_admin),
            MessageHandler(Filters.regex('^(' + admins + ')$'), admin_lists),
            MessageHandler(Filters.regex('^(' + users + ')$'), all_user),
            ],
        3: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, name_func)],
        4: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, text_func)],
        5: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, link_func)],
        6: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.photo, photo_func)],
        7: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, link_delete)],
        9: [MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, get_new_admin_name)],
        10: [MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.text, get_new_adminID)],
        11: [MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.text, get_new_admin_username)],
        8: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
            MessageHandler(Filters.text, rek)],
        12: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.regex('^(' + "📝 Text" + ')$'), rek_text1),
             MessageHandler(Filters.regex('^(' + "🎥 Video" + ')$'), rek_Video1),
             MessageHandler(Filters.regex('^(' + "🏞 Photo" + ')$'), rek_photo1),
             ],
        13: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.photo, rek_photo)],
        14: [CommandHandler('start', start),
            MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.video, rek_video)],
        15: [CommandHandler('start', start),
            CommandHandler('developer', developer),
             CallbackQueryHandler(inline_funcion_search),
             MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.text, fallback_text)
             ],
        50: [CommandHandler('start', start),
             CommandHandler('developer', developer),
             MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             CallbackQueryHandler(get_category_by_link),
             ],
        51: [CommandHandler('start', start),
             CommandHandler('developer', developer),
             MessageHandler(Filters.regex('^(' + menyu + ')$'), start),
             MessageHandler(Filters.photo, insert_full_link)
             ],
    },
    fallbacks=[CommandHandler('start', start),
        CommandHandler('developer', developer),
        MessageHandler(Filters.text, fallback_text)]
)

dispatcher.add_handler(all_handler)

updater.start_polling()

print("started BOT")
