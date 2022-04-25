import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode
import json
import requests
from Crypto.Cipher import AES
from base64 import b64encode,b64decode
from Crypto.Util.Padding import pad

def rsa_encrypt(message):
    key = open("D:\Python Codes\Keys\id_rsa.pub").read()
    key = key.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").replace("\n", "")
    key = b64decode(key)
    key = RSA.importKey(key)

    cipher = PKCS1_v1_5.new(key)
    ciphertext = b64encode(cipher.encrypt(bytes(message, "utf-8")))

    return ciphertext

message = "mohammed050"
key="aaaaaa5DA156D24a"
encrypted = rsa_encrypt(key)
print("EncryptedKey:",encrypted.decode('ascii'))

a=message				#text to be encrypted
ab=bytes(a,"utf-8")
iv="eeesixteenbyteiv"						#initialisation vector
ivb=bytes(iv,"utf-8")

data=ivb+ab
key="770A8A65DA156D24"		#key
key1=bytes(key,'utf-8')


cipher=AES.new(key1,AES.MODE_CBC,iv=ivb)
ct_bytes=cipher.encrypt(pad(data,AES.block_size,style="pkcs7"))
iv1 = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv1, 'ciphertext':ct})
print('EncryptedContent',result)
