"""Library of functions to cipher or uncipher files"""
from base64 import b64encode, b64decode
from binascii import unhexlify
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

