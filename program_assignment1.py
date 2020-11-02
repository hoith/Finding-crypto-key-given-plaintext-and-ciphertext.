import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import codecs
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
#from Crypto import Random
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad
#from Crypto.Util.Padding import unpad


plaintext = b"This is a top secret."
ciphertext = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"  
backend = default_backend()
iv = 16* chr(0)
def encrypt(key, pt):
	iv = 16* chr(0)
	padder = padding.PKCS7(128).padder()
	pt = padder.update(pt) + padder.finalize()
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(pt) + encryptor.finalize()
	return ct


def decrypt(key , ct):
	iv = 16* chr(0)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
	decryptor = cipher.decryptor()
	pt = decryptor.update(ct) + decryptor.finalize()
	return pt

#dictionary = open("words.txt", "r")
list = []
file = open("words.txt", "r")
lines = file.readlines()
for word in lines:
	if (len(word)> 16 ):
		continue
	else:
		list.append(word)

file.close()
for x in list:
	x =  x.rstrip("\n")
	if(len(x) > 16):
		continue
	padded_key = x.ljust(16)
	encrypted_text=encrypt(padded_key , plaintext)
	if (encrypted_text.encode("hex") == ciphertext):
		print("The correct key is", x)
