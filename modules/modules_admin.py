# Pixelbot
# Admin command module
# © 2021 Narek Torosyan

from telegram.ext import Updater, CommandHandler
import telegram

# helper function, not a command
def adminGate(update, context):
	bot = context.bot.get_chat_member(update.message.chat.id, context.bot.id)
	sender = context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
	if sender.status != "administrator" and sender.status != "creator":
		update.message.reply_text(text="You can't use this because you're not an admin.")
		return False
	if bot.status != "administrator" and bot.status != "creator":
		update.message.reply_text(text="You can't use this because I'm not an admin.")
		return False
	return True

# helper function, not a command
def selfGate(update, context, target, action):
	bot = context.bot.get_chat_member(update.message.chat.id, context.bot.id)
	sender = context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
	if target is sender:
		update.message.reply_text(text=f"You can't {action} yourself.")
		return False
	if target is bot:
		_alt = f"Attempt to use {bot.name} to {action} {bot.name} unsuccessful."
		update.message.reply_text(text=f"I can't {action} me.")
		return False
	return True

def ban(update, context):
	# admin protection
	if not adminGate(update, context):
		return
	# get target
	if update.message.reply_to_message:
		target = update.message.reply_to_message.from_user
	else:
		update.message.reply_text(text="Reply to someone to ban them!")
		return
	# self kick protection
	if not selfGate(update, context, target, "ban"):
		return

	update.effective_chat.kick_member(target.id)
	update.message.reply_text(text=f"{target.first_name} was banned!")

def unban(update, context):
	# admin protection
	if not adminGate(update, context):
		return
	# get target
	if update.message.reply_to_message:
		target = update.message.reply_to_message.from_user
	else:
		update.message.reply_text(text="Reply to someone to un-ban them!")
		return
	# self kick protection
	if not selfGate(update, context, target, "un-ban"):
		return

	update.effective_chat.unban_member(target.id)
	update.message.reply_text(text=f"{target.first_name} was un-banned!")

def kick(update, context):
	# admin protection
	if not adminGate(update, context):
		return
	# get target
	if update.message.reply_to_message:
		target = update.message.reply_to_message.from_user
	else:
		update.message.reply_text(text="Reply to someone to kick them!")
		return
	# self kick protection
	if not selfGate(update, context, target, "kick"):
		return

	update.effective_chat.unban_member(target.id)
	update.message.reply_text(text=f"{target.first_name} was kicked!")

CONTENTS=[
	CommandHandler('harderyeet', ban, run_async=True),
	CommandHandler('undotheyeet', unban, run_async=True),
	CommandHandler('sexyundoyeet', unban, run_async=True),
	CommandHandler('yeet', kick, run_async=True)
]