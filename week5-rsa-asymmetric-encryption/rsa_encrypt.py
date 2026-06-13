from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def rsa_encrypt(message):
    print("=== RSA Public Key Encryption Process ===")
    
    with open('public_key.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode())
    
    print(f"Original Message: {message}")
    print(f"Message Length: {len(message)} characters")
    print("Encrypting using Public Key...")
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}")
    print(f"Ciphertext Length: {len(ciphertext)} bytes")
    print("\nEncryption successful - message secured with public key!")
    return ciphertext

message = "CRYPTANALYSIS TOOLKIT - SECURE MESSAGE"
ciphertext = rsa_encrypt(message)