def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    keystream = []
    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])

    ciphertext = [ord(p) ^ k for p, k in zip(plaintext, keystream)]
    decrypted = [chr(c ^ k) for c, k in zip(ciphertext, keystream)]

    print("=== RC4 Stream Cipher ===")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    print(f"Keystream: {keystream[:len(plaintext)]}")
    print(f"Ciphertext (bytes): {ciphertext}")
    print(f"Decrypted: {''.join(decrypted)}")

rc4("SECURITY", "CRYPTANALYSIS")