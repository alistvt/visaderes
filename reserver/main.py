import logging
from pathlib import Path

from pyrogram import Client, filters

import cv
from reservation import reservation_handler, VisaType

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client(
  "anon",
  api_id=cv.API_ID,
  api_hash=cv.API_HASH
)


SCHENGEN_ADMINS_GROUP_ID = -1001602649099
LEGAL_ADMINS_GROUP_ID = -1001479871502
STUDENT_ADMINS_GROUP_ID = -1001731691531


@app.on_message(filters.me)
def my_pv_handler(client, message):
    print(message)
    text = message.text
    if 'تایید_مدارک_باز_شد' in text:
        reservation_handler.handle(VisaType.legal)
    elif 'ویزای_شینگن_باز_شد' in text:
        reservation_handler.handle(VisaType.schengen)
    elif 'ویزای_تحصیلی_باز_شد' in text:
        reservation_handler.handle(VisaType.student)
    

@app.on_message(filters.document)
def my_doc_handler(client, message):
    if message.from_user.id in cv.ADMIN_IDS:
        if not reservation_handler.validate_file_name(message.document.file_name):
            client.send_message(message.from_user.id, "invalid file name!")
        else:
            file_path = cv.BASE_FILES_PATH / message.document.file_name
            message.download(file_name=str(file_path))
            response = reservation_handler.validate_file(file_path)
            client.send_message(message.from_user.id, response)


@app.on_message(filters.group)
def my_group_handler(client, message):
    if message.chat.id in [-1001871799926, -1001610430560, -1001751602852]:
        text = message.text[:10].lower()
        sensitives = ['open', 'baz', 'باز']
        if any([x in text for x in sensitives]):
            if message.chat.id == -1001871799926:
                client.send_message(SCHENGEN_ADMINS_GROUP_ID, message.text)
            elif message.chat.id == -1001610430560:
                client.send_message(LEGAL_ADMINS_GROUP_ID, message.text)
            elif message.chat.id == -1001751602852:
                client.send_message(STUDENT_ADMINS_GROUP_ID, message.text)


@app.on_message(filters.channel)
def my_channel_handler(client, message):
    if message.chat.id == -1001761227448:
        text = message.text
        if 'وقت برای تایید مدارک موجود است.' in text:
            client.send_message(LEGAL_ADMINS_GROUP_ID, message.text)
        elif 'وقت مصاحبه برای ویزای شنگن موجود است.' in text:
            client.send_message(SCHENGEN_ADMINS_GROUP_ID, message.text)
        elif 'وقت مصاحبه برای ویزای تحصیلی موجود است.' in text:
            client.send_message(STUDENT_ADMINS_GROUP_ID, message.text)

    elif message.chat.id == -1001781509981:
        text = message.text
        if 'تایید_مدارک_باز_شد' in text:
            client.send_message(LEGAL_ADMINS_GROUP_ID, message.text)
            reservation_handler.handle(VisaType.legal)
        elif 'ویزای_شینگن_باز_شد' in text:
            client.send_message(SCHENGEN_ADMINS_GROUP_ID, message.text)
            reservation_handler.handle(VisaType.schengen)
        elif 'ویزای_تحصیلی_باز_شد' in text:
            client.send_message(STUDENT_ADMINS_GROUP_ID, message.text)
            reservation_handler.handle(VisaType.student)


app.run()