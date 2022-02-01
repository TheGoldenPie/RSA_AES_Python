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

encryptedKey = 'owSEY3r+9OPwemr6GCNCd1vs79xvP5YhaXtjj+IHOiScMmxVQTjqWAw5FyrsR1n51HsuNgOd/ESsi7AwMvnFl5T2hMInKuWufB04TWqqkyMSSPkLqdRDq9gnXSYDDxGiq+dqSY+FqqGJhDcqpcjNCYFzYUtB1VH66pV4m0/CKGTrX18yWLgl84dBp6ccd0Ynj/RCjltvpWb+u5u+KJWlM5VYRGlrquKMa6H1PqVhvZ7aOVO8IAEWQrYLNWtcit0xI8MmO/KRX657YRT6pYU0nFBHRNImxEZV8TQ3n0wAeU58kSmDiWYFys2ePVIuGzgAuWU8hoJc2qHCKjtr3QKkHJFxhimS7c8cm/bgfcPjDoE7hJdvkYN1FzmY3MqTB71l3jPO/oZq2/CJgGs/UcDXXaMeZkGE1lI1uFuGSqY4StqNU+C/QQe4eXaoRMsta6QDxidF4xveKfKjucHnRcrCIeyKV47NqLBQLw4OKRh/fs/fgXj67PpzBU2qnf/w+zZXAY94Ocw9lR33BnvQaalhOgeW9Jti7TMMMALBdiYmBikVKzo7KsRQJ3AuO/40RzIu7Jk3yVxX+w783ORxgLwsxJJnMexz2ATgvkwSljz8V6XZSi3eKwd+GCij2EivHs1G6DY6+CtCxPPXCN7HN2LlORoJk46cYXtO2guXTbA2PIU='
decrypted = rsa_decrypt(encryptedKey)
print('key',decrypted)

key=decrypted
key1=decrypted
print(len(key1))



ct1="N/LmrloJbGZ/iCHDOT63B/Bh/11+hCDCXboV0T0QmbwObZeCDCbBOfWKc3/tk2sATsapGByy4jnB06eoJOaL6ERVysq/P2o4p7kSLo8Y1ZOpWtZWRsJCqQD/WJxs4z7cRq6rK9J2I4jGNoiJid679QcG0WqRLenetRHAYJ6iuwjbUSTyIDsFHddWS8/VrBKMcpKb9i9X1m6E3qoxqs904midSAGblD4+X7E/7EvzxF+77S/V7rpfnT6hqVEvdpuQmElVfBTlUnRKHlm8i/DkWOrElkRyKsd50wu+Sv/pnPViNsQRVKr1Lq0SVD6pmHRW4jClnFUKn3G6/tGp0hwXSeQNBEtvuXpXtoxdDOqqeW7cANTHAWDQBz8XAry3gfSdEdY8TMXjxuwz3eonoDvqtbqwOzdu++5Z18nKOe2YFVZ4FTZgCDPNykVWC39eENjY"
ct2=bytes(ct1,"utf-8") 									#ct1 is the base64 encoded cipher text
ct = b64decode(ct2)
iv=ct[:16]
data=ct[16:]
cipher = AES.new(key1, AES.MODE_CBC,iv=iv)
pt = unpad(cipher.decrypt(data), AES.block_size)
print("The message was: ", pt.decode('ascii'))	
