# Pixelbot
# Joke command module
# © 2021 Narek Torosyan

from .module_text import ETA_ASKING, SLAP, SLAPPING, PUNCH, HUGLIST
from telegram.ext import Updater, CommandHandler
import telegram
import logging
import random
import time
from datetime import datetime, timedelta
from PIL import Image, ImageFont, ImageDraw

def etaWen(update, context):
    eta = update.message.reply_text(text=random.choice(ETA_ASKING))
    time.sleep(3)
    date = datetime.now() + timedelta(days=random.randrange(10, 450))
    eta.edit_text(date.strftime("%B %d, %Y") + "\n\nDate values might be inaccurate.")

def ram(update, context):
	bar = "░░░░░░░░░░░"
	eta = update.message.reply_text(text=f"Downloading 9999GB of RAM... {bar}")
	for i in range(bar):
		time.sleep(1)
		bar[i] = "█"
		eta.edit_text(f"Downloading 9999GB of RAM... {bar}")
	eta.edit_text(f"Your RAM is downloaded! {bar}")

def rickroll(update, context):
	update.message.reply_text(text="Click [here](https://www.youtube.com/watch?v=oHg5SJYRHA0)!", parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)

def stickbug(update, context):
	update.message.reply_text(text="Click [here](https://www.youtube.com/watch?v=fC7oUOUEEi4)!", parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)

def google(update, context):
	if update.message.reply_to_message:
		text = update.message.reply_to_message.text
		# Clean the text
		text = text.replace("Bro","").replace("Plz","").replace("Pls","").replace("Please","").replace("Sir","").replace("Ser","").replace("Bhai","")
		text = text.replace("bro","").replace("plz","").replace("pls","").replace("please","").replace("sir","").replace("ser","").replace("bhai","")
		# Remove spaces at the start and end
		text = text.lstrip().rstrip()
		# Do URL encoding
		text = text.replace(" ", "+").replace("(","%28").replace(")","%29")
		update.message.reply_text(text=f"[Google](https://www.google.com/search?q={text}&sclient=noob-ser) has the answer you need.", parse_mode=telegram.ParseMode.MARKDOWN)
	else:
		update.message.reply_text(text="Reply to a message to send someone to Google")

def slapName(user):
	if user.username:
		return "@"+user.username
	else:
		return user.first_name

def slap(update, context):
	slaper = update.message.from_user
	slapee = slaper
	if update.message.reply_to_message:
		slapee = update.message.reply_to_message.from_user
	item = random.choice(SLAP)
	spname = "themselves" if slapee == slaper else slapName(slapee)
	sl = random.choice(SLAPPING)
	if "{2}" in sl:
		sl = sl.format(slapName(slaper), spname, item).replace("themselves's","their")
	else:
		sl = sl.format(slapName(slaper), spname).replace("themselves's","their")
	update.message.reply_text(text=sl)

def hugmf(update, context):
 hugger = update.message.from_user
 huggee = hugger
 if update.message.reply_to_message:
  huggee = update.message.reply_to_message.from_user
 spname = "themselves" if huggee == hugger else slapName(huggee)
 sl = random.choice(HUGLIST)
 if "{1}" in sl:
  sl = sl.format(slapName(hugger), spname).replace("themselves's","their")
 else:
  sl = sl.format(slapName(hugger)).replace("themselves's","their")
 update.message.reply_text(text=sl)

def punch(update, context):
 puncher = update.message.from_user
 punchee = puncher
 if update.message.reply_to_message:
  punchee = update.message.reply_to_message.from_user
 spname = "themselves" if punchee == puncher else slapName(punchee)
 sl = random.choice(PUNCH)
 if "{1}" in sl:
  sl = sl.format(slapName(puncher), spname).replace("themselves's","their")
 else:
  sl = sl.format(slapName(puncher)).replace("themselves's","their")
 update.message.reply_text(text=sl)

def kil(update, context):
	punched = update.message.from_user
	if update.message.reply_to_message:
		punched = update.message.reply_to_message.from_user
	elif len(context.args) > 0:
		update.message.reply_text(text=context.args[0][1:])
		punched = update.message.chat.get_member(context.args[0][1:])
	else:
		# kill the sender
		punched = update.message.from_user
	# generate /kill message
	name = punched.first_name
	if punched.username:
		name = punched.username
	W,H = (512,288)
	msg = f"{name} fell out of the world"
	img = Image.open("resources/ded.png")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("resources/mc.ttf", 12)
	w, h = draw.textsize(msg, font=font)
	draw.text(((W-w)/2,((H-h)/2)-42),msg,(255,255,255),font=font)
	img.save('sample-out.webp')
	# send it
	update.message.reply_sticker(sticker=open('sample-out.webp', 'rb'))

CONTENTS = [
	CommandHandler('eta', etaWen, run_async=True),
	CommandHandler('ram', ram, run_async=True),
	CommandHandler('rr', rickroll, run_async=True),
	CommandHandler('sb', stickbug, run_async=True),
	CommandHandler('searchurselfretard', google, run_async=True),
	CommandHandler('google', google, run_async=True),
	CommandHandler('punch', punch, run_async=True),
	CommandHandler('slap', slap, run_async=True),
	CommandHandler('kill', kil, run_async=True),
	CommandHandler('hug', hugmf, run_async=True)
]