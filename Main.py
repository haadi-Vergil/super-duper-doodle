import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

CHANNEL_USERNAME = "@NETHRA_IPTV"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Check if user is a member of the channel
    member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)
    status = member.status

    if status in ["member", "administrator", "creator"]:
        await update.message.reply_text(f"Welcome, {user.first_name}! You are authorized to use this bot.")
    else:
        await update.message.reply_text(
            f"⚠️ You must join {CHANNEL_USERNAME} to use this bot.\n"
            f"Please join the channel and then send /start again."
        )

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()
