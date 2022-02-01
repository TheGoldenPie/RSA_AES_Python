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
    #key = b64decode("MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsIwVStQi6aSMLBZu3vhafOR5NTMNp+TXPwyk/6VoaSQfDnZaSQPYhdt4a8X215KwXwpIL1eBJOH2NW8jp5AO4WauHWEwEggJvPaC8FgzZtDhjYexOk+/yaDbY7U9BofJSU76VIBxRoN7YmAknAKrpfn0ukXPPuUx5Ny/cy85nunqo5M8Acf2VVwSGZQMBZFSm3yxYOdS4laDlM+s1w+5wLDMjYSgIMm76rpVdO3hs2n2dSAYM6XMOaqNDwHdZk6n8lPgivYVXjTz7KU9eqkFnecWvn2ugRI7hgrplZxS020k0QBeYd0AH7zJZKS3Xo5VycL01UO/WYOQvB7v8lge7TiQZ3CCrnuykqcJ/r5DMLO/cKQAeZi+LQ95FQg39joO8G7bfO7+a3Gs8Re3mRW7AA8x1aEn7XZMOUu4l4IfNvwh20V4cz3xvGXdr9ZLFvgX5593MxCDBjkiaynzG8gmLVTIoaItPy+khwO/vjfWka0L3yvT3l55R4H/KRKxlHaY58HVdLbuWrUoH/4gbkYFYFC+rejBW5wbE0FJmWIkEXLKsTlXcsn6eAzi4BRxidQ/4rIEf8qWpSFzJobivBnWe4bpBA19g3N47PDpD5xS6uj7ODSBhEn22UnsiDaGV+RhsXYA/xqaJCjB6+W7CN00Lowr87sUoT4VAK8wrOk4D5sCAwEAAQ==")
    key = b64decode(key)
    key = RSA.importKey(key)

    cipher = PKCS1_v1_5.new(key)
    ciphertext = b64encode(cipher.encrypt(bytes(message, "utf-8")))

    return ciphertext

message = "{\"amount\": 10,\"tranRefNo\": \"ICICI66283873\",\"localTxnDtTime\": \"20220118112748\",\"mobile\": \"8884735786\",\"beneIFSC\": \"DLXB0000092\",\"paymentRef\": \"ICICI66283873\",\"senderName\": \"Test Sender\",\"bcID\": \"IBCKer00055\",\"beneAccNo\": \"000405002777\",\"retailerCode\": \"rcode\",\"passCode\": \"447c4524c9074b8c97e3a3c40ca7458d\"}"
key="770A8A65DA156D24"
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
