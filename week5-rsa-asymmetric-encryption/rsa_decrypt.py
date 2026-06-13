from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def rsa_decrypt(ciphertext):
    print("=== RSA Private Key Decryption Results ===")
    
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    
    print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()[:80]}...")
    print("Decrypting using Private Key...")
    print(f"Decrypted Message: {plaintext.decode()}")
    print("\nDecryption successful - original message recovered!")
    return plaintext

# Encrypt first then decrypt to show full cycle
with open('public_key.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

message = "CRYPTANALYSIS TOOLKIT - SECURE MESSAGE"
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message.encode())

rsa_decrypt(ciphertext)