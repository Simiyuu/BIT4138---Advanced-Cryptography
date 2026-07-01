def diffie_hellman_exchange(p, g, alice_private, bob_private):
    print("=== Diffie-Hellman Key Exchange ===\n")
    print(f"Public Prime (p): {p}")
    print(f"Generator (g):    {g}\n")

    print(f"Alice's Private Key: {alice_private}")
    print(f"Bob's Private Key:   {bob_private}\n")

    alice_public = (g ** alice_private) % p
    bob_public = (g ** bob_private) % p

    print(f"Alice's Public Key (g^a mod p): {alice_public}")
    print(f"Bob's Public Key (g^b mod p):   {bob_public}\n")

    alice_secret = (bob_public ** alice_private) % p
    bob_secret = (alice_public ** bob_private) % p

    print(f"Alice computes Shared Secret (B^a mod p): {alice_secret}")
    print(f"Bob computes Shared Secret (A^b mod p):   {bob_secret}\n")

    print("=== Verification ===")
    if alice_secret == bob_secret:
        print(f"SUCCESS: Both parties derived the same shared secret: {alice_secret}")
        print("This shared secret can now be used as a symmetric encryption key.")
    else:
        print("ERROR: Secrets do not match!")

    return alice_secret, bob_secret

p = 23
g = 5

alice_private = 6
bob_private = 15

diffie_hellman_exchange(p, g, alice_private, bob_private)