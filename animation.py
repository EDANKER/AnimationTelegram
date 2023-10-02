import time
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

app_id = ""
app_hash = ""

client = Client(name="edankr_yzo", api_hash=app_hash, api_id=app_id)

@client.on_message(filters.command("anim", prefixes="!") & filters.me)
def type(client_object, message: Message):
    input_text = message.text.split("!anim ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "⁂"

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.05)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.05)
        except FloodWait:
            print("лимит привышен")

client.run()