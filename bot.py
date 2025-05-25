from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# এখানে আপনার টেলিগ্রাম বট API টোকেনটি বসানো হয়েছে
BOT_TOKEN = "7809984946:AAExF5P82832exrW3kLkQ4KNNOu6XKzQ7qQ"

# /start কমান্ডের জন্য ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "স্বাগতম! আমি আপনার টেলিগ্রাম বট। /help লিখে আমার কমান্ডগুলো দেখতে পারেন।"
    )

# /help কমান্ডের জন্য ফাংশন
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "আমি যা করতে পারি:\n"
        "/start - বট চালু করুন\n"
        "/help - সাহায্য মেসেজ দেখুন\n"
        "আপনি যেকোনো মেসেজ পাঠান, আমি রিপ্লাই দিব!"
    )

# সাধারণ মেসেজ হ্যান্ডল করার ফাংশন
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"আপনি বললেন: {user_message}")

# অজানা কমান্ড হ্যান্ডল করার ফাংশন
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("দুঃখিত, আমি এই কমান্ডটি চিনতে পারিনি।")

# মূল অংশ (বট চালু করার জন্য)
if __name__ == "__main__":
    # বট অ্যাপ্লিকেশন তৈরি করা হচ্ছে
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # কমান্ড হ্যান্ডলার যোগ করা হচ্ছে
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # সাধারণ টেক্সট মেসেজ হ্যান্ডলার
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # অজানা কমান্ড হ্যান্ডলার
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # বট চালু করুন
    print("Bot is running...")
    app.run_polling()