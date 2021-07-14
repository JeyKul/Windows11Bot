# Pixelbot
# Main file
# © 2021 Narek Torosyan

# Import libraries
from telegram.ext import Updater, CommandHandler
import telegram
import logging
# Import the command packs, to use the commands in them
from modules import modules_joke, modules_useful, modules_admin
from config import TOKEN
import config

VERSION = 12
FORM = "https://forms.gle/HMy57F8zqHwKHzfb6"

HELLO = """
Hello!

I'm Windows11_Bot, a bot originally created by @thegreatporg and modiefied by @JeyKul based on ideas from @pixel2020_official and @OT9810. The main topic of me is Windows 11.
I'm in development. You can suggest commands for me with /suggest.
I'm also open source. Check the source code with /source.
Last but not least, you can support my creators by checking out /donate.
"""

CREDITS = """
@thegreatporg - developer
@JeyKul - hoster

Credits for commands in Pixelbot:
- @tthalheim for /root and /rootsam
- XDA for /blokada
- the @pixel2020_official community for /magisk
"""

DONATION = """
Want to support the people behind Galaxy and Pixelbot? That's nice :3

Support the developer of Pixelbot on [ko-fi](https://ko-fi.com/thegreatporg).
Support the hoster of Pixelbot on [ko-fi](https://ko-fi.com/jeykul).{}
"""
# Command code
def start(update, context):
	update.message.reply_text(text=HELLO)

def changes(update, context):
	f = open("changes.txt", "r")
	text = f.read()
	update.message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)
	f.close()

def help_cmd(update, context):
	f = open("help.txt", "r")
	text = f.read()
	update.message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)
	f.close()

def credits(update, context):
	update.message.reply_text(text=CREDITS)

def oss(update, context):
	update.message.reply_text(text="Click [here](https://github.com/JeyKul/modifiedpixelbot) to see my source!", parse_mode=telegram.ParseMode.MARKDOWN)

def feats(update, context):
	update.message.reply_text(text=f"To suggest features, topics and helpful Magisk modules (for /modules) fill and submit [this]({FORM}) form.", parse_mode=telegram.ParseMode.MARKDOWN)

def donate(update, context):
	don = DONATION
	if config.DONATION_URLS:
		don = don.format(f"\nAnd, support the maintainers of this fork: {', '.join(config.DONATION_URLS)}.")
	else:
		don = don.format("")
	update.message.reply_text(text=don, parse_mode=telegram.ParseMode.MARKDOWN)

def download(update, context):
    text = open("download.txt").read()
    update.message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2, disable_web_page_preview=True)

# Create updater and dispatcher 
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# Add handlers for built in commands
dispatcher.add_handler(CommandHandler('start', start, run_async=True))
dispatcher.add_handler(CommandHandler('help', help_cmd, run_async=True))
dispatcher.add_handler(CommandHandler('changes', changes, run_async=True))
dispatcher.add_handler(CommandHandler('credits', credits, run_async=True))
dispatcher.add_handler(CommandHandler('source', oss, run_async=True))
dispatcher.add_handler(CommandHandler('suggest', feats, run_async=True))
dispatcher.add_handler(CommandHandler('donate', donate, run_async=True))
dispatcher.add_handler(CommandHandler('download', download, run_async=True))
# Add joke command handlers
print("Importing joke commands")
for h in modules_joke.CONTENTS:
	dispatcher.add_handler(h)
# Add useful command handlers
print("Importing useful commands")
for h in modules_useful.CONTENTS:
	dispatcher.add_handler(h)
# Add admin command handlers
print("Importing admin commands")
for h in modules_admin.CONTENTS:
	dispatcher.add_handler(h)
# Print a message
print(f"Galaxybot {VERSION} started!")
# Update
updater.start_polling()
