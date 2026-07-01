import binascii

def vulnerable_encrypt(plaintext, key):
    return bytes([plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext))])

def extract_key(known_plaintext, ciphertext, key_length):
    recovered_key = bytearray(key_length)
    for i in range(key_length):
        recovered_key[i] = known_plaintext[i] ^ ciphertext[i]
    return bytes(recovered_key)

def run_kpa_simulation():
    print("=== Known Plaintext Attack (KPA) Simulator ===")
    
    secret_key = b'HACK' 
    full_message = b"CONFIDENTIAL: The server password is 'Admin123!'"
    ciphertext = vulnerable_encrypt(full_message, secret_key)
    
    print("[*] Intercepted Ciphertext (hex):")
    print(f"    {binascii.hexlify(ciphertext).decode()}")
    print("-" * 50)
    
    print("[!] Initiating Known Plaintext Attack...")
    known_fragment = b"CONFIDENTIAL" 
    
    print(f"[*] Assuming Known Plaintext Fragment: '{known_fragment.decode()}'")
    
    assumed_key_length = 4
    recovered_key = extract_key(known_fragment[:assumed_key_length], ciphertext, assumed_key_length)
    
    print(f"[+] CRITICAL SUCCESS: Secret Key Recovered -> '{recovered_key.decode()}'")
    print("-" * 50)
    
    print("[!] Decrypting full intercepted payload using recovered key...")
    decrypted_message = vulnerable_encrypt(ciphertext, recovered_key)
    
    print(f"[+] Decrypted Payload: {decrypted_message.decode()}")

run_kpa_simulation()