"""Library of functions to cipher or uncipher files"""

import base64
from Cryptodome.Cipher import AES
from cryptography.fernet import Fernet

def encrypt_message(message, key):
    """Function to cipher a plain text using AES128"""
    length = 16 - (len(message) % 16)
    message += bytes([length])*length
    initial_vector = message[:16]
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return cipher.encrypt(message)

def decrypt_message(cipher_text, key, initial_vector):
    """Function to decipher a ciphered text using AES128"""
    decipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return decipher.decrypt(cipher_text)

def encrypt(text, key):
    """Library to encrypt manually"""
    key = base64.urlsafe_b64encode(key)
    fernet = Fernet(key)
    return fernet.encrypt(text)

def decrypt(file, key):
    """Library to decrypt manually"""
    fernet = Fernet(key)
    with open(file, 'rb') as keyfile:
        encrypted = keyfile.read()
    decrypted = fernet.decrypt(encrypted)
    return bytes.hex(decrypted)
