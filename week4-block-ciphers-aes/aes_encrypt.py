from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def aes_encrypt(key, plaintext):
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    print("=== AES Encryption Script ===")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    print(f"IV: {binascii.hexlify(cipher.iv).decode()}")
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}")
    return cipher.iv, ciphertext

key = "SECURITYKEY12345"
message = "CRYPTANALYSIS TOOLKIT"
aes_encrypt(key, message)