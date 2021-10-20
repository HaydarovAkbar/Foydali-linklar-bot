from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from connect import Database

Token = "2033346371:AAHr_v7iPC-3xjuZSTBhAnpL50leIgB7Dn8"
web, bot, kanal, boshqa, haqida, add = "🌏 Web sayt linklari♻️", "🌏 Bot linklari♻️", "🌏 Kanal linklari♻️", "🌏 Boshqa linklari♻️", "🤖 Bot haqida 📝", "Qo'shish"
menu = ReplyKeyboardMarkup([
    [web, kanal],
    [bot, boshqa],
    [haqida, add]
], resize_keyboard=True)

dba = Database()

def test(start=0,cat=1):
    try:
        all_link_data = dba.get_link_catID(cat)
        data = all_link_data[start:start + 10]
        battons, b = [], []
        if len(all_link_data) - start > start:
            end_num = start +10
        elif start > len(all_link_data):
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
    ["Menyu"]
], resize_keyboard=True)

reklama_admin = ReplyKeyboardMarkup([
    ["📝 Text", "🎥 Video"],
    ["🏞 Photo", "Menyu"]
], resize_keyboard=True)
admins_key = ReplyKeyboardMarkup([
    ["Add link", "Delete link"],
    ["Add reklama", "Users", "Add admin"],
    ["Admins", "Menyu"]
], resize_keyboard=True)

category_key = ReplyKeyboardMarkup([
    ["🌏WebSayt qo'shish", "🌏Kanal qo'shish"],
    ["🌏Bot qo'shish", "🌏Boshqa link"],
    ["Menyu"]
], resize_keyboard=True)
