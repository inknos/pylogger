from Crypto.Cipher import AES
import base64
from head import *

msg_text = 'test some plain text here'.rjust(32)
try:
  encrypt_key
except NameError:
  encrypt_key = '1234567890123456' # create new & store somewhere safe


def crypt(to_encrypt):
  cipher = AES.new(encrypt_key, AES.MODE_ECB) # never use ECB in strong systems obviously
  encoded = base64.b64encode(cipher.encrypt(to_encrypt))
  return encoded


def decrypt(to_decrypt):
  cipher = AES.new(encrypt_key, AES.MODE_ECB) # never use ECB in strong systems obviously
  decoded = cipher.decrypt(base64.b64decode(encoded))
  return decoded


#print encoded
# ...
#print decoded.strip()
