from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

def encrypt_file(input_file, key):
    with open(input_file, 'r') as f:
        plaintext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    
    with open('secret_encrypted.bin', 'wb') as f:
        f.write(cipher.iv + ciphertext)
    
    print("=== File Encryption Demonstration ===")
    print(f"Original File: {input_file}")
    print(f"Plaintext: {plaintext}")
    print(f"Key (hex): {binascii.hexlify(key).decode()}")
    print("Encrypted file saved as: secret_encrypted.bin")
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}")

key = get_random_bytes(16)
encrypt_file('secret.txt', key)