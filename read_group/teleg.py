
import logging
from datetime import datetime, timedelta
from time import sleep
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


SCHENGEN_ADMINS_GROUP_ID = -1001602649099
LEGAL_ADMINS_GROUP_ID = -1001479871502
STUDENT_ADMINS_GROUP_ID = -1001731691531

app = Client(
  "anon",
  api_id=740627,
  api_hash="8c6ce28b5242d893e4cb7c93ea3eb437"
)

@app.on_message(filters.me)
def my_handler(client, message):
    print(message)


@app.on_message(filters.group)
def my_handler(client, message):
    # if message.from_user.id == 665660679:
    # print(message.chat.id)
    if message.chat.id == -1001761227448:
      if 'وقت برای تایید مدارک موجود است.' in text:
        client.send_message(LEGAL_ADMINS_GROUP_ID, message.text)
      elif 'وقت مصاحبه برای ویزای شنگن موجود است.' in text:
        client.send_message(SCHENGEN_ADMINS_GROUP_ID, message.text)
      elif 'وقت مصاحبه برای ویزای تحصیلی موجود است.' in text:
        client.send_message(STUDENT_ADMINS_GROUP_ID, message.text)
      
    elif message.chat.id in [-1001871799926, -1001610430560, -1001751602852]:
      text = message.text[:10].lower()
      sensitives = ['open', 'baz', 'باز']
      if any([x in text for x in sensitives]):
        if message.chat.id == -1001871799926:
          client.send_message(SCHENGEN_ADMINS_GROUP_ID, message.text)
        elif message.chat.id == -1001610430560:
          client.send_message(LEGAL_ADMINS_GROUP_ID, message.text)
        elif message.chat.id == -1001751602852:
          client.send_message(STUDENT_ADMINS_GROUP_ID, message.text)

app.run()