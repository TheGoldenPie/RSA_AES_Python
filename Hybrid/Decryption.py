from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode
import json
import requests
from Crypto.Cipher import AES
from base64 import b64encode,b64decode
from Crypto.Util.Padding import unpad
import codecs
import unicodedata

def rsa_decrypt(encryptedKey):
    key = open("D:\Python Codes\Keys\privatekey.pub").read()
    key = key.replace("-----BEGIN RSA PRIVATE KEY-----", "").replace("-----END RSA PRIVATE KEY-----", "").replace("\n", "")
    key = b64decode(key)
    key = RSA.importKey(key)

    cipher = PKCS1_v1_5.new(key)
    plaintext = cipher.decrypt(b64decode(encryptedKey), "Error while decrypting")

    return plaintext

encryptedKey = 'Add Your Encrypted Key here'
decrypted = rsa_decrypt(encryptedKey)
print('key',decrypted)

key=decrypted
key1=decrypted
print(len(key1))



ct1="Add your Encrypted Data Here"
ct2=bytes(ct1,"utf-8") 									#ct1 is the base64 encoded cipher text
ct = b64decode(ct2)
iv=ct[:16]
data=ct[16:]
cipher = AES.new(key1, AES.MODE_CBC,iv=iv)
pt = unpad(cipher.decrypt(data), AES.block_size)
print("The message was: ", pt.decode('ascii'))	
