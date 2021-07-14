# Pixelbot
# Useful command module
# © 2021 Narek Torosyan

from .module_text import BLOKADA
from telegram.ext import Updater, CommandHandler
import telegram
from androlib import asb
from bs4 import BeautifulSoup
import requests
from config import PIRACY
import os.path
from os import path

ADB_ERROR = """
There is no single /adb command.

Use:
/adbL for Linux
/adbM for Mac
/adbW for Windows
"""

def blokada(update, context):
	update.message.reply_text(text=BLOKADA, parse_mode=telegram.ParseMode.MARKDOWN)

def bulletin(update, context):
	data = asb.getLatestASB()
	spl = ""
	if len(data["spl"][0]) == 1:
		spl = data["spl"]
	else:
		for l in data["spl"]:
			spl = f"{spl},{l}"
		spl = spl.lstrip(",")
	crunch = f'*Latest Android Security Bulletin - {data["date"]}*\n*Published on:* {data["publishedOn"]}\n*SPL(s):* {spl}\n[Read more]({data["url"]})'
	update.message.reply_text(text=crunch, parse_mode=telegram.ParseMode.MARKDOWN)


def freezer(update, context):
	# legal safeguard
	if not PIRACY:
		print("/freezer has been disabled due to law.")
		print("If storing piracy apps is legal in your country set PIRACY to True in config.py.")
		update.message.reply_text(text="Enabling /freezer requires extra steps by the bot's hoster.")
		return
	# though is storing instructions on how to download said apps legal?
	ms = update.message.reply_text(text="_Downloading Freezer..._", parse_mode=telegram.ParseMode.MARKDOWN)
	x = requests.get("https://www.freezer.life/")
	soup = BeautifulSoup(x.content, 'html.parser')
	dl = soup.select("#android > div > div > div:nth-child(2) > p:nth-child(5) > a:nth-child(3)")
	url = dl[0].get("href")
	fn = "freezer/"+url.split("/")[len(url.split("/"))-1]
	if not path.exists(fn):
		print(f"New Freezer version {fn.replace('freezer/','').replace('.apk','')}!")
		ms.edit_text(text=f"Found new Freezer version `{fn.replace('freezer/','').replace('.apk','')}`!\n_Downloading..._", parse_mode=telegram.ParseMode.MARKDOWN)
		print("Downloading...", end='')
		r = requests.get(url, allow_redirects=True)
		print(" done.\nWriting...", end='')
		open(fn, 'wb').write(r.content)
		print(" done.")
	ms.edit_text(text="_Uploading APK...\nThis might take a while. You will get a new reply when it's done._", parse_mode=telegram.ParseMode.MARKDOWN)
	update.message.reply_document(document=open(fn, 'rb'), caption="The latest Freezer APK for `arm64`.\n*Do not use it if playing copyrighted music for personal use is illegal in your country! IF YOU GET IN TROUBLE, THE PIXELBOT DEVS WON'T BE RESPONSIBLE! USE AT YOUR OWN RISK!*", timeout=60, parse_mode=telegram.ParseMode.MARKDOWN)
	ms.delete()

CONTENTS = [
	CommandHandler('blokada', blokada, run_async=True),
	CommandHandler('asb', bulletin, run_async=True),
	CommandHandler('freezer', freezer, run_async=True)
]