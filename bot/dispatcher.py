from telegram.ext import CommandHandler
from bot.commands.start import start_command

def setup_bot(app):
    app.add_handler(CommandHandler("start", start_command))
