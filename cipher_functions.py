"""Library of functions to cipher or uncipher files"""

import base64
import random
from Cryptodome.Cipher import AES
from cryptography.fernet import Fernet

def encrypt_message(message, key):
    """Function to cipher a plain text using AES128"""
    length = 16 - (len(message) % 16)
    message += bytes([length])*length
    initial_vector = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
    initial_vector = bytes(initial_vector, 'utf-8')[:16]
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return cipher.encrypt(message)

def decrypt_message(message, key):
    """Function to decipher a ciphered text using AES128"""
    initial_vector = message[:16]
    decipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return decipher.decrypt(message)

def encrypt(text, key):
    """Library to encrypt manually"""
    key = base64.urlsafe_b64encode(key)
    fernet = Fernet(key)
    return fernet.encrypt(text)

def decrypt(file, key):
    """Library to decrypt manually"""
    key = base64.urlsafe_b64encode(key)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(file)
    return bytes.hex(decrypted)
