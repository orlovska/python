import telebot

bot = telebot.TeleBot("920195982:AAGbdzO5nmiNLiifQS3ztfaCrXq1lpU6xiY")

# Let's define a message handler
# which handles incoming /start and /help commands.
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, "42/n https://youtu.be/aboZctrHfK8?t=82")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


# To start the bot, add the following to our source file:
bot.polling()

