"""Library of functions to cipher or uncipher files"""

import base64
from Cryptodome.Cipher import AES
from Cryptodome import Random
from cryptography.fernet import Fernet

def encrypt_manual(message, key):
    """Function to encrypt a plain text using AES256"""
    pad = (AES.block_size - len(message) % AES.block_size)\
                * chr(AES.block_size - len(message) % AES.block_size)
    message = message + bytes(pad, "utf-8")
    initial_vector = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return initial_vector + cipher.encrypt(message)

def decrypt_manual(message, key):
    """Function to decrypt a ciphered text using AES128"""
    initial_vector = message[:AES.block_size]
    decipher = AES.new(key, AES.MODE_CBC, initial_vector)
    data = decipher.decrypt(message)
    return data[:-ord(data[len(data) - 1:])]

def encrypt(text, key):
    """Library to encrypt manually"""
    key = base64.urlsafe_b64encode(key)
    fernet = Fernet(key)
    return fernet.encrypt(text)

def decrypt(text, key):
    """Library to decrypt manually"""
    key = base64.urlsafe_b64encode(key)
    fernet = Fernet(key)
    return fernet.decrypt(text)
