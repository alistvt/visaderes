# Import pyTelegramBotApi ==> a module for create a bot on telegram
import telebot
# Import request ==> a library to get data on web
import requests
# Import json ==> a module to work with json
import json
import yaml
# Create the bot
TOKEN = "6286763064:AAGI6iEzcX9Uv5Kw1By3etReg7lmlq81EuI"
BOT = telebot.TeleBot(TOKEN)
cities=['اراک','اردبیل','ارومیه','اصفهان','اهواز','ایلام','بجنورد','بندرعباس','بوشهر','بیرجند','تبریز','تهران']

# Start bot with /start command
@BOT.message_handler(commands=['start'])
def start(message):
    BOT.send_message(message.from_user.id, "به ربات مدیریت فایل خوش آمدید❤️")
    BOT.send_message(message.from_user.id, "لطفا فایل مورد نظر راباپسوند yaml ارسال کنید")


# Send a photo by user
@BOT.message_handler(content_types=['document'])
def get_document(message):
    file_name = message.document.file_name
    file_type = file_name.split('.')[-1]
    #print(file_type)
    if file_type.lower() == "yaml":
        file_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(
            TOKEN,
            BOT.get_file(message.document.file_id).file_path
        )
        file = requests.get(file_url)
        open(f"files/{file_name}", "wb").write(file.content)
        data = yaml.safe_load(file.content)
        city = data['city']
        if city not in cities:
            BOT.send_message(chat_id=message.chat.id,text="شهر مشکل دارد",parse_mode="HTML")
        BOT.send_message(
            chat_id=message.chat.id,
            text="فایل مورد نظر با موفقیت ذخیره شد",
            parse_mode='HTML'
        )
    else:
        BOT.send_message(
            chat_id=message.chat.id,
            text="لطفا فایل را با پسوند yaml بفرستید",
            parse_mode='HTML'
        )


# Run bot
BOT.infinity_polling()