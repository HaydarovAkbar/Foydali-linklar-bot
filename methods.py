from battons import *
from connect import Database
from datetime import datetime
import time

date = "20:10:2021"
database = Database()

music_start = [0]
cat_list = [0]


def start(update, context):
    user = update.message.chat
    dat = database.get_id()
    d = [i[0] for i in dat]
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'Assalomu alaykum <b>{name}</b>!😊\n'
                                  f'\n<b><u>Foydali linklarni ulashuvchi botga Xush kelibsiz</u></b>\n'
                                  f'<i>Endi sizga kerakli barcha\n✅<b>Web saytlar\n✅Kanal,Gruppalar\n✅Botlar\n♻️ Va Boshqa kerakli linklarni</b>\n'
                                  f"Bir botdan topishingiz mumkin</i>!\n"
                                  f"Va o'zingizni linklaringizni qo'shishingiz mumkin!😎\n\n"
                                  f"🗒Botni ishlatish bo'yicha qo'llanmani ko'rish 👉@kerakli_linklar_kanal\n\n"
                                  f"Qidirayotgan link nomini yoki unda qatnashgan so'zni yuboring!",
                             parse_mode="HTML",
                             reply_markup=menu)
    if user.id not in d:
        database.set_user(user.first_name, user.id, user.username)
    return 1


def battons1(update, context):
    global cat_list
    global music_start
    cat_list.clear()
    music_start.clear()
    music_start.append(0)
    cat_list.append(1)
    if not test(music_start[-1], cat_list[-1])[1]:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Malumotlar bush")
        return 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=test(music_start[-1], cat_list[-1])[1],
                             reply_markup=test(music_start[-1], cat_list[-1])[0])
    return 1


def battons2(update, context):
    global cat_list
    global music_start
    cat_list.clear()
    cat_list.append(2)
    music_start.clear()
    music_start.append(0)
    if not test(music_start[-1], cat_list[-1])[1]:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Malumotlar bush")
        return 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=test(music_start[-1], cat_list[-1])[1],
                             reply_markup=test(music_start[-1], cat_list[-1])[0])
    return 1


def battons3(update, context):
    global cat_list
    global music_start
    cat_list.clear()
    cat_list.append(3)
    music_start.clear()
    music_start.append(0)
    if not test(music_start[-1], cat_list[-1])[1]:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Malumotlar bush")
        return 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=test(music_start[-1], cat_list[-1])[1],
                             reply_markup=test(music_start[-1], cat_list[-1])[0])
    return 1


def battons4(update, context):
    global cat_list
    global music_start
    cat_list.clear()
    cat_list.append(4)
    music_start.clear()
    music_start.append(0)
    if not test(music_start[-1], cat_list[-1])[1]:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Malumotlar bush")
        return 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=test(music_start[-1], cat_list[-1])[1],
                             reply_markup=test(music_start[-1], cat_list[-1])[0])
    return 1


def battons5(update, context):
    user = database.get_users()
    coun = len(database.get_link())
    count = len(user)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"<b>1.🧮Hozirda Botdan Foydalanuvchilar soni: <u>{count}</u>\n\n"
                                  f"2. 🗑Botdagi jami linklar soni : <u>{coun}</u>\n\n"
                                  f"3.📅Botni ishga tushirilgan vaqti: <u>{date}</u>\n\n"
                                  f"4.👨‍💻Dasturchi bilan aloqa:</b> @Akbar_TUIT\n\n",
                             parse_mode="HTML",
                             reply_markup=about)
    return 1


def battons6(update, context):
    user = update.message.chat.id
    admins = database.get_admin()
    admins_id = [i[2] for i in admins]
    if user in admins_id:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Admin Xush kelibsiz:😊",
                                 reply_markup=admins_key)
        return 2
    else:
        return add_link(update, context)


def add_link(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Siz qo'shayotgan ma'lumotlar <b>Ishonchli va to'liq</b> "
                                  "bo'lishini so'rab qolamiz aks holda qo'shgan ma'lumotlaringiz Adminlar "
                                  "tominidan o'chirilishi mumkin👮‍♀️"
                                  "\nQo'shish bo'yicha qo'llanma ushbu Kanalda berib o'tilgan 👉@kerakli_linklar_kanal"
                                  "\n\n<b><u>Qaysi Kategoriyadagi link qo'shmoqchisiz Tanlang</u></b>:",
                             parse_mode="HTML",
                             reply_markup=category_key)
    user_auto.clear()
    return 2


def add_delete_linkID(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"O'chiriladigan link IDsini kiriting:")
    return 7


def link_delete(update, context):
    id = update.message.text
    if id.isdigit():
        i = database.getID_link(int(id))
        try:
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=i[2],
                                   caption=f"""<b>{i[6]}</b>:\n\n<i>{i[1]}</i>\n\n<b>Link</b>: {i[3]}""",
                                   disable_notification=True,
                                   parse_mode="HTML")
            ababab = "<b>Yuqoridagi 'LINK' o'chirildi!</b>"
        except Exception as e:
            print(e)
            ababab = "<b>'LINK' o'chirildi!</b>"
        a = database.delete_link(int(id))
        if a:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=ababab,
                                     parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Linkni o'chirishda qanaqadir muammo bo'ldi!")
    return 2


def reklama(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Menga xabar jo'natishingiz mumkin men uni hammaga jo'nataman!</b>"
                                  "\nQuyidagi Kategoryilardan birini tanlang!",
                             parse_mode="HTML",
                             reply_markup=reklama_admin)
    return 12


def rek_text1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Text Faylni jo'natishingiz mumkin!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 8


def rek(update, context):
    user_id = update.message.from_user.id
    text = update.message.text
    if user_id in [s[2] for s in database.get_admin()]:
        s = 0
        for item in database.get_id():
            try:
                context.bot.send_message(chat_id=item[0], text=text + "\n\n    @kerakli_linklar_bot")
                s += 1
            except Exception as e:
                print(e)
        context.bot.send_message(chat_id=user_id,
                                 text=f"Jo'natgan  xabaringiz {s}-ta userga bordi!",
                                 reply_markup=about)
        return 2
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Uzr sizni tanimadim🧐",
                                 reply_markup=about)
    return 1


def rek_photo1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Photo Faylni jo'natishingiz mumkin!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 13


def rek_photo(update, context):
    user_id = update.message.from_user.id
    caption = update.message.caption
    photo = update.message.photo[0]["file_id"]
    if photo:
        if user_id in [s[2] for s in database.get_admin()]:
            s = 0
            for item in database.get_id():
                try:
                    context.bot.send_photo(chat_id=item[0],
                                           photo=photo,
                                           caption=caption + "\n\n    @kerakli_linklar_bot",
                                           disable_notification=True)
                    s += 1
                except Exception as e:
                    print(e)
            context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=about)
            return 2
        else:
            context.bot.send_message(chat_id=user_id,
                                     text=f"Uzr sizni tanimadim🧐",
                                     reply_markup=about)
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Rasm jo'natishingiz kerak edi adashdingiz!",
                                 reply_markup=about)
        return 1


def rek_Video1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Video Faylni jo'natishingiz mumkin!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 14


def rek_video(update, context):
    user_id = update.message.from_user.id
    text = update.message.caption
    video = update.message.video['file_id']
    if video:
        if user_id in [s[2] for s in database.get_admin()]:
            s = 0
            for item in database.get_id():
                try:
                    context.bot.send_video(chat_id=item[0],
                                           video=video,
                                           caption=text + "\n\n    @kerakli_linklar_bot",
                                           disable_notification=True)
                    s += 1
                except Exception as e:
                    print(e)
            context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=about)
            return 2
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Video jo'natishingiz kerak edi adashdingiz",
                                 reply_markup=about)
        return 1


def sub_message_delete(update, context):
    try:
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"<b>Siz allaqachon ro'yxat boshidasiz</b>!!!",
                                     parse_mode="HTML")
        time.sleep(1.5)
        context.bot.delete_message(
            timeout=60,
            chat_id=(a.chat.id),
            message_id=int(a.message_id))
    except Exception as e:
        print(e)


def add_message_delete(update, context):
    try:
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"<b>Siz allaqachon ro'yxat Oxiridasiz</b>!!!",
                                     parse_mode="HTML")
        time.sleep(1.5)
        context.bot.delete_message(
            timeout=60,
            chat_id=(a.chat.id),
            message_id=int(a.message_id))
    except Exception as e:
        print(e)


def inline_funcion(update, context):
    try:
        query = update.callback_query
        global music_start
        global cat_list
        if query.data == "chapga":
            if music_start[-1] == 0:
                return sub_message_delete(update, context)
            else:
                mus = music_start[-1]
                music_start.append(mus - 10)
                a = test(music_start[-1], cat_list[-1])
                query.edit_message_text(text=a[1], reply_markup=a[0])
        elif query.data == "delete":
            query.delete_message(timeout=15)
        elif query.data == "ungga":
            mus = music_start[-1]
            mus += 10
            music_start.append(mus)
            a = test(music_start[-1], cat_list[-1])
            if not a:
                mus = music_start[-1]
                music_start.append(mus - 10)
                return add_message_delete(update, context)
            query.edit_message_text(text=a[1], reply_markup=a[0])
        else:
            query.edit_message_text(text="✅")
            i = database.getID_link(int(query.data))
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=i[2],
                                   caption=f"""{i[0]}). <b>{i[6]}</b>\n\n<i>{i[1]}</i>\n\n<b><u>Link: 👉 </u></b>{i[3]}\n\n      @kerakli_linklar_bot""",
                                   disable_notification=True,
                                   parse_mode="HTML", )
            return 1
    except Exception as e:
        return 1


user_auto = []


def category_web(update, context):
    user_auto.append(1)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Web sayt nomini aniq,tushinarli va qisqa kiriting!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 3


def category_bot(update, context):
    user_auto.append(3)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Bot nomini aniq,tushinarli va qisqa kiriting</b>!",
                             parse_mode="HTML",
                             reply_markup=about)
    return 3


def category_channel(update, context):
    user_auto.append(2)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Kanal yoki Gruppa nomini aniq,tushinarli va qisqa kiriting!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 3


def category_boshqa(update, context):
    user_auto.append(4)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Boshqa tipdagi link nomini aniq,tushinarli va qisqa kiriting!</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 3


def name_func(update, context):
    name = update.message.text
    user_auto.append(name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Link orqali nima qilish mumkinligini va bu malumotlar boshqalarga"
                                  " qanaqa foyda keltirishini <u>Imlo xatolarsiz kiriting</u></b>!",
                             parse_mode="HTML",
                             reply_markup=about)
    return 4


def text_func(update, context):
    text = update.message.text
    user_auto.append(text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Linkni kiritishingiz mumkin:)</b>",
                             parse_mode="HTML",
                             reply_markup=about)
    return 5


def link_func(update, context):
    link = update.message.text
    user_auto.append(link)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b><u>Kanal,WebSayt,Bot yoki malumotingiz</u></b> aks etgan rasm kiritishingiz mumkin!",
                             parse_mode="HTML",
                             reply_markup=about)
    return 6


def photo_func(update, context):
    photo = update.message.photo[0]["file_id"]
    user = update.message.chat.id
    t = datetime.now()
    time = str(t)
    a = database.set_link(user_auto[2], photo, user_auto[3], user, time, user_auto[1], user_auto[0])
    if a:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="<b>Ma'lumotlar muvaffaqiyatli bazaga saqlandi\nRahmat sizga!!!😊</b>",
                                 parse_mode="HTML",
                                 reply_markup=about)
    return 7


# Admin qo'shish funkisayalari
admin_list = []


def add_admin(update, context):
    first_name = update.message.from_user.first_name
    admin_list.clear()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Admin qo'shmoqchimisiz <b>{first_name}</b>\n  Yangi adminning Ismini yuboring :)!",
                             parse_mode="HTML",
                             reply_markup=about)
    return 9


def get_new_admin_name(update, context):
    try:
        admin_list.append(update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Yangi adminning  ID raqamini yuboring :)!")
        return 10
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")


def get_new_adminID(update, context):
    try:
        admin_id = update.message.text
        if admin_id.isdigit():
            admin_list.append(int(admin_id))
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Yangi adminning <b>username</b> bo'lsa yuboring aks holda '.' yuboring:)!",
                                     parse_mode="HTML")
            return 11
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Siz ID kiritmadingiz:(",
                                     reply_markup=about)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
        return


def get_new_admin_username(update, context):
    try:
        admin_list.append(update.message.text)
        print(admin_list)
        A = database.add_admin(admin_list[0], admin_list[1], admin_list[2])
        print(A)
        if A:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Yangi admin Muvafaqiyatli qo'shildi:)!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Yangi admin qo'shilmadi:)!")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
    return 2


def admin_lists(update, context):
    try:
        name = update.message.from_user.first_name
        admin_text = name + "Adminlar ro'yxati:)\n\n"
        for i in database.get_admin():
            count = len(database.get_link_userID(i[2]))
            admin_text += f"{i[0]}. {i[1]}  @{i[3]}\n Qo'shgan linklari soni:{count}\n\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=admin_text)
    except Exception as e:
        print(e)


music_start_search = [0]
textlar = [""]
def inline_funcion_search(update, context):
    try:
        query = update.callback_query
        global music_start_search
        global textlar
        text = textlar[-1]
        d = database.get_link_text(text)
        if query.data == "chapga":
            if music_start_search[-1] == 0:
                return sub_message_delete(update, context)
            else:
                mus = music_start_search[-1]
                music_start_search.append(mus - 10)
                a = test_0(music_start_search[-1],d)
                query.edit_message_text(text=a[1], reply_markup=a[0])
        elif query.data == "delete":
            query.delete_message(timeout=15)
            return 1
        elif query.data == "ungga":
            mus = music_start_search[-1]
            mus += 10
            music_start_search.append(mus)
            a = test_0(music_start_search[-1],d)
            if not a:
                mus = music_start_search[-1]
                music_start_search.append(mus - 10)
                return add_message_delete(update, context)
            query.edit_message_text(text=a[1], reply_markup=a[0])
        else:
            query.edit_message_text(text="✅")
            i = database.getID_link(int(query.data))
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=i[2],
                                   caption=f"""{i[0]}). <b>{i[6]}</b>\n\n<i>{i[1]}</i>\n\n<b><u>Link:</u></b> 👉 {i[3]}\n\n      @kerakli_linklar_bot""",
                                   disable_notification=True,
                                   parse_mode="HTML", )
            textlar = []
            music_start_search = [0]
            return 1
    except Exception as e:
        return 1

def fallback_text(update, context):
    global textlar
    global music_start_search
    try:
        text = update.message.text
        data = database.get_link_text(text)
        if data:
            music_start_search = [0]
            textlar.append(text)
            start = music_start_search[-1]
            bat = test_0(start,data)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=bat[1],
                                     reply_markup=bat[0])
            return 15
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Siz kiritgan so'zlar qatnashgan linklar Afsuski topilmadi!",
                                     reply_markup=about)
        return 1
    except Exception as e:
        print(e)


def all_user(update, context):
    all_user = database.get_users()[-50:]
    all_text = "{:<1} || {:<8} || {:<23}\n\n".format("Number", "Name", "Username")
    for item in all_user:
        try:
            all_text += "{:<1}). || <b>{:<8}</b> || @{:<23}\n".format(item[0], item[1], item[3])
        except:
            pass
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=all_text,
                             parse_mode="HTML",
                             reply_markup=about)

def developer(update, context):
    try:
        now = datetime.today()
        res = (now - datetime(2000,11,25)).days // 365 + 1
        a = context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"<b>About developer:\n\nFull Name: Akbar Haydarov\nAge: {res}\nMa'lumoti: TATU 3-kurs\nUsername: @Akbar_TUIT\n...!</b>",
                                     parse_mode="HTML")
    except Exception as e:
        print(e)
