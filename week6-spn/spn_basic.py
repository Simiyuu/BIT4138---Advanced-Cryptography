SBOX = {0: 14, 1: 4, 2: 13, 3: 1,
        4: 2, 5: 15, 6: 11, 7: 8,
        8: 3, 9: 10, 10: 6, 11: 12,
        12: 5, 13: 9, 14: 0, 15: 7}

PERMUTATION = [3, 0, 2, 1]

def substitute(nibble):
    return SBOX[nibble]

def permute(bits):
    result = ['0'] * 4
    for i, pos in enumerate(PERMUTATION):
        result[pos] = bits[i]
    return ''.join(result)

def spn_encrypt(plaintext, key):
    print("=== Basic SPN Encryption ===")
    print(f"Plaintext: {plaintext} (binary: {bin(plaintext)})")
    print(f"Key: {key}")

    mixed = plaintext ^ key
    print(f"\nAfter Key Mixing (XOR): {mixed} (binary: {bin(mixed)})")

    substituted = substitute(mixed % 16)
    print(f"After Substitution (S-Box): {substituted} (binary: {bin(substituted)})")

    bits = format(substituted, '04b')
    permuted = permute(bits)
    print(f"After Permutation: {permuted} (binary)")

    ciphertext = int(permuted, 2) ^ key
    print(f"\nFinal Ciphertext: {ciphertext} (binary: {bin(ciphertext)})")
    return ciphertext

plaintext = 9
key = 5
spn_encrypt(plaintext, key)