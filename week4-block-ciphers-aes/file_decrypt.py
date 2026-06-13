from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def encrypt_file(input_file, key):
    with open(input_file, 'r') as f:
        plaintext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    
    with open('secret_encrypted.bin', 'wb') as f:
        f.write(cipher.iv + ciphertext)
    
    print("=== AES Encryption Results ===")
    print(f"Original File: {input_file}")
    print(f"Key (hex): {binascii.hexlify(key).decode()}")
    print("Encrypted file saved as: secret_encrypted.bin")
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}\n")

def decrypt_file(encrypted_file, key):
    with open(encrypted_file, 'rb') as f:
        data = f.read()
    
    iv = data[:16]
    ciphertext = data[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    print("=== AES Decryption Results ===")
    print(f"Encrypted File: {encrypted_file}")
    print(f"IV (hex): {binascii.hexlify(iv).decode()}")
    print(f"Decrypted Plaintext: {plaintext.decode()}")
    print("Decryption successful - original message recovered!")

master_key = get_random_bytes(16)

encrypt_file('secret.txt', master_key)

decrypt_file('secret_encrypted.bin', master_key)