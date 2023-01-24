from telegram import Update
from telegram.ext import (
    CallbackContext,
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

# 1. await get data from db
# 2. assign data to variable
# 3. push data to db
# 4. something else

application = Application.builder().token("5827036837:AAF2CBl5WTSqaKZ456bvmtkkLlBVpLzI5UA").build()  # to be in one line


async def startCommand(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hello! I am a telegram bot for the dry run !")  # telegram requires that whatever is done by the API is awaited


async def mimicMessage(update: Update, context: CallbackContext):
    incomingMessage = update.message.text
    await update.message.reply_text(incomingMessage)


application.add_handler(CommandHandler("start", startCommand))
application.add_handler(MessageHandler(filters=filters.TEXT, callback=mimicMessage))
application.run_polling()
