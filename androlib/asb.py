# AndroLib
# for Pixelbot
# Functions for getting Android/Pixel security bulletins
# © 2021 Narek Torosyan

from bs4 import BeautifulSoup
import requests
import re

asb_url = "https://source.android.com/security/bulletin"
psb_url = "https://source.android.com/security/bulletin/pixel"

def getLatestASB():
	x = requests.get(asb_url)
	soup = BeautifulSoup(x.content, 'html.parser')
	tr = soup.table.find_all('tr')[1]
	return parseASB(tr)

def getEveryASB():
	x = requests.get(asb_url)
	soup = BeautifulSoup(x.content, 'html.parser')
	tr = soup.table.find_all('tr')
	asbs = []
	for t in tr:
		asbs.append(parseASB(t))
	return asbs

def getLatestPixelSB():
	x = requests.get(psb_url)
	soup = BeautifulSoup(x.content, 'html.parser')
	tr = soup.table.find_all('tr')[1]
	return parseASB(tr)

def getEveryPixelSB():
	x = requests.get(psb_url)
	soup = BeautifulSoup(x.content, 'html.parser')
	tr = soup.table.find_all('tr')
	asbs = []
	for t in tr:
		asbs.append(parseASB(t))
	return asbs

def parseASB(tr):
	ret = {}
	tds = tr.find_all('td')
	ret["date"] = tds[0].a.string
	ret["url"] = "https://source.android.com" + tds[0].a.get("href")
	ret["publishedOn"] = tds[2].string
	for linebreak in tds[3].find_all('br'):
	    linebreak.extract()
	tdt = re.sub("<\/?td>", "", str(tds[3]))
	if "\n" in tdt:
	    ret["spl"] = tdt.split()
	else:
	    ret["spl"] = tdt
	return ret
