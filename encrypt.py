"""

following this example from
http://docs.python-guide.org/en/latest/scenarios/crypto/

from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
decoded_text = cipher_suite.decrypt(encoded_text)

NOT safe cryptographic way!!! DIDACTIC PURPOSE

"""

from cryptography.fernet import Fernet


class simpleCrypt:
    def __init__(self, key = "abcde"):
        self.key = key
        self.key = 'F8tcioZ_84LHMZO4AzM0oM3apM3TRbWVon4Xqsq7qUE='
        #Fernet.generate_key() #this is your "password"
        self.cipher_suite = Fernet(self.key)

    def encode(self, text=""):
        return self.cipher_suite.encrypt(bytes(text))
    
    def decode(self, text=""):
        return self.cipher_suite.decrypt(bytes(text))
    
