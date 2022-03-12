from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from connect import Database

Token = "1982825247:AAHZtL5XKfS9FTXBfUm5CS_IbG0Rq4S0Zfc"

web, bot, kanal, boshqa, haqida, add = "🌏 Web sayt linklari♻️", "🌏 Bot linklari♻️", "🌏 Kanal linklari♻️", "🌏 Boshqa linklari♻️", "🤖 Bot haqida 📝", "Qo'shish"
add_link_txt, del_link, add_rek, users,add_admin_txt = "➕ Add link", "🪓 Delete link", "✖️ Add reklama","🚹 Users","🛂 Add admin"
admins, menyu = "🛗 Admins", "🌐 Menyu"
add_web_sayt,add_channel,add_bot, add_other_link = "🌏WebSayt qo'shish","🌏Kanal qo'shish","🌏Bot qo'shish","🌏Boshqa link"
full_join_link = '©️ Tayyor link 🔵'

menu = ReplyKeyboardMarkup([
    [web, kanal],
    [bot, boshqa],
    [haqida, add]
], resize_keyboard=True)

dba = Database()


def test(start=0,cat=1):  # 50  88
    try:
        all_link_data = dba.get_link_catID(cat)[::-1]
        data = all_link_data[start:start + 10]
        battons, b = [], []
        if len(all_link_data) - start > 10:
            end_num = start +10
        elif start >= len(all_link_data):
            return False
        else:
            end_num = len(all_link_data)
        all_name, c = f"Natijalar {start+1}-{end_num}:   {len(all_link_data)} dan\n\n", 1
        for i in data:
            all_name += f"{c}. {i[6]}\n"
            if len(b) < 5:
                b.append(InlineKeyboardButton(f"{c}", callback_data=f"{i[0]}"))
            else:
                battons.append(b)
                b = [InlineKeyboardButton(f"{c}", callback_data=f"{i[0]}")]
            c += 1
        battons.append(b)
        battons.append([InlineKeyboardButton(f"⬅️", callback_data="chapga"),
                        InlineKeyboardButton(f"️❌", callback_data="delete"),
                        InlineKeyboardButton(f"️➡", callback_data="ungga")])
        bat = InlineKeyboardMarkup(battons)
        result = [bat, all_name,all_link_data]
        return result
    except Exception as e:
        return False
def test_0(start=0,d=None): # 50 --- 88
    try:
        all_link_data = d[::-1]
        data = all_link_data[start:start + 10]
        battons, b = [], []
        if len(all_link_data) - start > 10:
            end_num = start +10
        elif start >= len(all_link_data):
            return False
        else:
            end_num = len(all_link_data)
        all_name, c = f"Natijalar {start+1}-{end_num}:   {len(all_link_data)} dan\n\n", 1
        for i in data:
            all_name += f"{c}. {i[6]}\n"
            if len(b) < 5:
                b.append(InlineKeyboardButton(f"{c}", callback_data=f"{i[0]}"))
            else:
                battons.append(b)
                b = [InlineKeyboardButton(f"{c}", callback_data=f"{i[0]}")]
            c += 1
        battons.append(b)
        battons.append([InlineKeyboardButton(f"⬅️", callback_data="chapga"),
                        InlineKeyboardButton(f"️❌", callback_data="delete"),
                        InlineKeyboardButton(f"️➡", callback_data="ungga")])
        bat = InlineKeyboardMarkup(battons)
        result = [bat, all_name,all_link_data]
        return result
    except Exception as e:
        return False

about = ReplyKeyboardMarkup([
    [menyu]
], resize_keyboard=True)

reklama_admin = ReplyKeyboardMarkup([
    ["📝 Text", "🎥 Video"],
    ["🏞 Photo", "Menyu"]
], resize_keyboard=True)
admins_key = ReplyKeyboardMarkup([
    [add_link_txt,full_join_link, del_link],
    [add_rek , users, add_admin_txt],
    [admins, menyu]
], resize_keyboard=True)

category_key = ReplyKeyboardMarkup([
    [add_web_sayt,add_channel ],
    [add_bot, add_other_link],
    [menyu]],
    resize_keyboard=True)

def all_category_by_link():
    batton = InlineKeyboardMarkup([
        [InlineKeyboardButton(add_web_sayt,callback_data=1),
         InlineKeyboardButton(add_bot,callback_data=3),],
        [InlineKeyboardButton(add_channel,callback_data=2),
         InlineKeyboardButton(add_other_link,callback_data=4),]
    ])
    return batton
