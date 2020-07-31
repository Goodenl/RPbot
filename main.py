import os
import re
import telebot

# Изменить!
api_token = "1331026510:AAFDJtzfgSsKnM43R1ilvokVgrg8oAkThHI"
api = os.getenv("RP_API_TOKEN")

path_to_write = os.getenv("RP_PATH")
episod_number = "Эпизод 1"

bot = telebot.TeleBot(api_token)

#save all message in file
def save_message(text):
	with open(f"{path_to_write}{episod_number}\\temp.txt", "a") as w:
		w.write(f"{text}\n")
		w.close()

@bot.message_handler(content_types=["text"])
def send_var(message):
	bot.send_message(message.chat.id, message)

	save_message(message.text)


bot.polling(none_stop=True)