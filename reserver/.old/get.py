from telethon import TelegramClient, events
import yaml
import reserves
import reservet
import reservetahsili


# telegram api code
api_id = 740627
api_hash = '8c6ce28b5242d893e4cb7c93ea3eb437'

#make telegram client with proxy
#if this code run on foreign serever(out of iran) dont need proxy
client = TelegramClient(
    'anon',
    api_id,
    api_hash
)


@client.on(events.NewMessage)
async def my_event_handler(event):
    text1 = str(event.message.message)
    text2=event.message
    #channelid = event.message.peer_id.channel_id
    # print(text1)

    if 'تایید_مدارک_باز_شد' in text1:
        
        ret = reservet.BOT()
        ret.login(city,payment_cart,payment_date,sheba,sheba_owner,first_name,last_name,birth_year,birth_month,birth_date,passport,phone,email)
    elif 'ویزای_شینگن_باز_شد' in text1:
        yaml_file = open("files/s.yaml", 'r', encoding='utf8')
        data = yaml.safe_load(yaml_file)
        city = data['city']
        payment_cart = data['payment_cart']
        payment_date = data['payment_date']
        sheba = data['sheba']
        sheba_owner = data['sheba_owner']
        first_name = data['first_name']
        last_name = data['last_name']
        birth_year = data['birth_year']
        birth_month = data['birth_month']
        birth_date = data['birth_date']
        passport = data['passport']
        phone = data['phone']
        email = data['email']
        res = reserves.BOT()
        res.login(city, payment_cart, payment_date, sheba, sheba_owner, first_name, last_name, birth_year, birth_month,
                 birth_date, passport, phone, email)
    # elif 'رزروتحصیلی' in text1:
    #     yaml_file = open("files/vt.yaml", 'r', encoding='utf8')
    #     data = yaml.safe_load(yaml_file)
    #     city = data['city']
    #     payment_cart = data['payment_cart']
    #     payment_date = data['payment_date']
    #     sheba = data['sheba']
    #     sheba_owner = data['sheba_owner']
    #     first_name = data['first_name']
    #     last_name = data['last_name']
    #     birth_year = data['birth_year']
    #     birth_month = data['birth_month']
    #     birth_date = data['birth_date']
    #     passport = data['passport']
    #     phone = data['phone']
    #     email = data['email']
    #     reta = reservetahsili.BOT()
    #     reta.login(city, payment_cart, payment_date, sheba, sheba_owner, first_name, last_name, birth_year, birth_month,
    #               birth_date, passport, phone, email)


#send post to processor that extract text


client.start()
client.run_until_disconnected()
