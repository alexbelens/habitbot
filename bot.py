from bot.dispatcher import setup_bot
from telegram.ext import Application
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    setup_bot(app)
    print("HabitBot запущен.")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
