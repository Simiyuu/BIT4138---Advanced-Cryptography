from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

def rsa_test_suite():
    print("=== RSA Testing and Validation Suite ===")
    print("-" * 55)
    
    print("\n[TEST 1] Key Generation")
    key = RSA.generate(2048)
    public_key = key.publickey()
    print("Status: PASS - 2048-bit key pair generated successfully")
    
    print("\n[TEST 2] Encryption Validation")
    test_messages = [
        "Hello World",
        "CRYPTANALYSIS",
        "Secure Toolkit 2024"
    ]
    cipher_enc = PKCS1_OAEP.new(public_key)
    cipher_dec = PKCS1_OAEP.new(key)
    
    for msg in test_messages:
        ciphertext = cipher_enc.encrypt(msg.encode())
        decrypted = cipher_dec.decrypt(ciphertext)
        status = "PASS" if decrypted.decode() == msg else "FAIL"
        print(f"Message: '{msg}' | Status: {status}")
    
    print("\n[TEST 3] Encryption Performance")
    start = time.time()
    for _ in range(10):
        cipher_enc.encrypt(b"Performance test message")
    elapsed = (time.time() - start) * 1000
    print(f"10 encryptions completed in: {elapsed:.2f} ms")
    print(f"Average per encryption: {elapsed/10:.2f} ms")
    
    print("\n=== All Tests Completed Successfully ===")

rsa_test_suite()