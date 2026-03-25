from telegram.ext import Updater, CommandHandler

BOT_TOKEN = "8655800213:AAFGX9TuBjW4ySZ-VzMsGdREVtyf-BZcu0U"
DOWNLOAD_URL = "https://gofile.io/d/V1xYss"

def start(update, context):
    user_id = update.effective_chat.id
    update.message.reply_text(
        f"🔴 SWILL COLLECTOR\n\n📥 Завантажити: {DOWNLOAD_URL}\n\n🆔 Ваш ID: <code>{user_id}</code>",
        parse_mode='HTML'
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("🤖 Бот запущено!")
    updater.idle()

if __name__ == "__main__":
    main()
