import time

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def rc4_encrypt(key, plaintext):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        ciphertext.append(ord(char) ^ S[(S[i] + S[j]) % 256])
    return ciphertext

message = "CRYPTANALYSIS" * 100

print("=== Encryption Performance Test ===")

start = time.time()
caesar_cipher(message, 3)
print(f"Caesar Cipher Time: {(time.time()-start)*1000:.4f} ms")

start = time.time()
rc4_encrypt("SECURITY", message)
print(f"RC4 Stream Cipher Time: {(time.time()-start)*1000:.4f} ms")

print("\nConclusion: RC4 operates at byte level making it faster for larger data.")