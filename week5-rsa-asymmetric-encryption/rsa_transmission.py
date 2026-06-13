from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def simulate_secure_transmission(sender_message):
    print("=== Secure Message Transmission Simulation ===")
    print("-" * 50)
    
    print("[RECEIVER] Generating RSA key pair...")
    key = RSA.generate(2048)
    public_key = key.publickey()
    print("[RECEIVER] Public key shared with sender.")
    
    print(f"\n[SENDER] Original Message: {sender_message}")
    print("[SENDER] Encrypting message with receiver's public key...")
    cipher_encrypt = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_encrypt.encrypt(sender_message.encode())
    print(f"[SENDER] Encrypted Message (hex): {binascii.hexlify(ciphertext).decode()[:80]}...")
    print("[SENDER] Encrypted message transmitted successfully.")
    
    print("\n[RECEIVER] Decrypting message with private key...")
    cipher_decrypt = PKCS1_OAEP.new(key)
    decrypted = cipher_decrypt.decrypt(ciphertext)
    print(f"[RECEIVER] Decrypted Message: {decrypted.decode()}")
    print("\nSecure transmission complete - only the receiver could decrypt!")

simulate_secure_transmission("CONFIDENTIAL: Cryptanalysis Toolkit Test Message")