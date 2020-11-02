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
import random
import string


def Average(lst): 
    return sum(lst) / len(lst)

message_hash = hashlib.sha256()
message =hashlib.sha256(b"This is really secure.").hexdigest()
#print(message)
new_message = message[0:3]
#print(new_message)
average_array1 = []
average_array2 = []
#Weak collison
print("WEAK COLLISON-------------------------------------")
for i in range(100):
	count=0
	count2 = 0 
	rand_string1 = string.ascii_letters
	rand_string1= ''.join(random.choice(rand_string1) for i in range(10))
	message =hashlib.sha256(rand_string1).hexdigest() # set different random every run
	new_message = message[0:3]
	while(count>-1):
		count=count+1
		rand_string2 = string.ascii_letters
		rand_string2= ''.join(random.choice(rand_string1) for i in range(10))
		rand_message =hashlib.sha256(rand_string2).hexdigest() # randomize until we get match
		new_randmessage = rand_message[0:3]
		if ( new_message == new_randmessage):
			print("Match found at count ",count)
			average_array1.append(count)
			break;
print ("AVERAGE: ", Average(average_array1))

print("STRONG COLLISON-------------------------------------")
for i in range(100):
	count=0
	count2 = 0 
	store_hash = []
	while(count>-1):
		count=count+1
		rand_string1 = string.ascii_letters
		rand_string1= ''.join(random.choice(rand_string1) for i in range(10))
		message =hashlib.sha256(rand_string1).hexdigest() # set different random every run
		new_message = message[0:3]
		rand_string2 = string.ascii_letters
		rand_string2= ''.join(random.choice(rand_string1) for i in range(10))
		rand_message =hashlib.sha256(rand_string2).hexdigest() # randomize until we get match
		new_randmessage = rand_message[0:3]
		store_hash.append(new_randmessage)
		if new_message in store_hash:
			print("Match found at count ",count)
			average_array2.append(count)
			break;

print ("AVERAGE: ", Average(average_array2))