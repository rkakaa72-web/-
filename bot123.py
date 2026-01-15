import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "bot_token"
CHANNEL_TARGET = 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

START_TEXT = (
    "Одним сообщением напиши то что указано в анкете\n\n"
    "<pre>
    "АНКЕТА"
    "???:"
    "???:"
    "???:"
    "<pre>"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(START_TEXT, parse_mode="HTML")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Напиши /start — пришлю шаблон анкеты ещё раз.")

async def forward_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    
    await update.message.forward(chat_id=CHANNEL_TARGET)

   
    

def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))


    app.add_handler(MessageHandler(~filters.COMMAND & filters.ALL, forward_any_message))

    app.run_polling()

if __name__ == "__main__":
    main()