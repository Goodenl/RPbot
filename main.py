import os
import telebot
import mega_upload as mu


api_token = os.getenv("RP_API_TOKEN")

path_to_write = os.getenv("RP_PATH")
episod_number = "Episod 1"

bot = telebot.TeleBot(api_token)

counter_package = 0

#save all message in file
def save_message(text, counter):
	
	if not(text.startswith("\\")):

		with open(f"{path_to_write}{episod_number}\\temp.txt", "a", encoding="utf-8") as w:
			w.write(f"{text}\n")
			w.close()

	#upload on server
	counter += 1
	if counter == 5:
		mu.upload_on_cloud() # Как оно работает??
		counter = 0

@bot.message_handler(content_types=["text"])
def get_message(message):
	if message.chat.type == "private":
		bot.send_message(message.chat.id, message.text)

		save_message(message.text, counter_package)
	else:
		save_message(message.text, counter_package)


bot.polling(none_stop=True)