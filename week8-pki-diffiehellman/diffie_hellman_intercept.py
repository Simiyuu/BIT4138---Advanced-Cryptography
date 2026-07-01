p = 23 
g = 5  


alice_private = 6
bob_private = 15

eve_private = 2

print("--- HONEYPOT ALERT: MITM INTERCEPTION DETECTED ---")

alice_public = (g ** alice_private) % p
bob_public = (g ** bob_private) % p

eve_public = (g ** eve_private) % p
print(f"[!] Threat Actor intercepted Alice's Key ({alice_public}) and Bob's Key ({bob_public})")
print(f"[!] Threat Actor injected Spoofed Key ({eve_public}) to both parties.")

alice_shared_secret = (eve_public ** alice_private) % p
bob_shared_secret = (eve_public ** bob_private) % p

eve_shared_with_alice = (alice_public ** eve_private) % p
eve_shared_with_bob = (bob_public ** eve_private) % p

print("\n--- ENCRYPTION KEYS NEGOTIATED ---")
print(f"Alice believes she shares a key with Bob: {alice_shared_secret}")
print(f"Eve's actual shared key with Alice:       {eve_shared_with_alice}")
print(f"Bob believes he shares a key with Alice:  {bob_shared_secret}")
print(f"Eve's actual shared key with Bob:         {eve_shared_with_bob}")

print("\n[RESULT] Complete compromise. The threat actor can now decrypt, log, and re-encrypt all traffic seamlessly.")