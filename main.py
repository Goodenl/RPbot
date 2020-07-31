import json
import os
import telebot
# import mega_upload as mu

# Изменить!
api_token = os.getenv("RP_API_TOKEN")

path_to_write = os.getenv("RP_PATH")
episod_number = "Episod 1"

bot = telebot.TeleBot(api_token)

#save all message in file
def save_message(text):
	if not(text.startswith("\\")):

		with open(f"{path_to_write}{episod_number}\\temp.txt", "a", encoding="utf-8") as w:
			w.write(f"{text}\n")
			w.close()

@bot.message_handler(content_types=["text"])
def get_message(message):
	bot.send_message(message.chat.id, message.text)

	save_message(message.text)

	# mu.upload_on_cloud()


bot.polling(none_stop=True)