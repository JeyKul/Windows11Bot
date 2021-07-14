# Pixelbot
# PXB parser
# © 2021 Narek Torosyan

ADMIN = 0x0100
JOKE = 0x0010
USEFUL = 0x0001
PORN = 0x1000
PATH = "groups.pxb"

def getFeatureNumber(groupID):
	with open(PATH,"r") as f:
		for l in f.readlines():
			if l.startswith(f"{groupID}="):
				return l.replace(f"{groupID}=", "")

def saveFeatures(groupId, features):
	fn = 0
	for fe in features:
		fn = fn + fe
	with open(PATH,"a+") as f:
		f.write(f"{groupId}={fn}\n")

def getFeatures(num):
	entit = []
	for c in [ADMIN,USEFUL,JOKE,PORN]:
		if (num & c) == c:
			entit.append(c)
	return entit

def getGroupFeatures(groupId):
	return getFeatures(int(getFeatureNumber(groupId)))