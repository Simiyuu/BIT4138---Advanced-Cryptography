import time

def feistel_round(left, right, key):
    new_left = right
    new_right = left ^ (right + key)
    return new_left, new_right

def feistel_encrypt(plaintext, key, rounds=4):
    left = plaintext >> 4
    right = plaintext & 0xF
    for _ in range(rounds):
        left, right = feistel_round(left, right, key)
    return (left << 4) | right

SBOX = {0: 14, 1: 4, 2: 13, 3: 1,
        4: 2, 5: 15, 6: 11, 7: 8,
        8: 3, 9: 10, 10: 6, 11: 12,
        12: 5, 13: 9, 14: 0, 15: 7}

PERMUTATION = [3, 0, 2, 1]

def spn_round(plaintext, key):
    mixed = plaintext ^ key
    substituted = SBOX[mixed % 16]
    bits = format(substituted, '04b')
    result = ['0'] * 4
    for i, pos in enumerate(PERMUTATION):
        result[pos] = bits[i]
    return int(''.join(result), 2) ^ key

def spn_encrypt(plaintext, key, rounds=4):
    result = plaintext
    for _ in range(rounds):
        result = spn_round(result, key)
    return result

def evaluate():
    print("=== SPN vs Feistel Security Evaluation ===")
    print("-" * 55)

    plaintext = 9
    key = 5
    test_count = 10000

    start = time.time()
    for _ in range(test_count):
        feistel_encrypt(plaintext, key)
    feistel_time = (time.time() - start) * 1000

    start = time.time()
    for _ in range(test_count):
        spn_encrypt(plaintext, key)
    spn_time = (time.time() - start) * 1000

    print(f"\n[PERFORMANCE TEST] ({test_count} encryptions)")
    print(f"Feistel Encryption Time: {feistel_time:.4f} ms")
    print(f"SPN Encryption Time:     {spn_time:.4f} ms")

    print("\n[STRUCTURE COMPARISON]")
    print(f"{'Property':<30} {'Feistel':<20} {'SPN'}")
    print("-" * 65)
    print(f"{'Data Processing':<30} {'Half block':<20} {'Full block'}")
    print(f"{'Decryption':<30} {'Same structure':<20} {'Inverse operations'}")
    print(f"{'Non-Linearity':<30} {'Round function':<20} {'S-Box based'}")
    print(f"{'Modern Example':<30} {'DES':<20} {'AES'}")
    print(f"{'Rounds Needed':<30} {'More rounds':<20} {'Fewer rounds'}")

    print("\n[SECURITY EVALUATION]")
    print("Feistel Result: {feistel_encrypt(plaintext, key)}")
    print("SPN Result:     {spn_encrypt(plaintext, key)}")
    print("\nConclusion: SPN processes the full block each round,")
    print("providing stronger diffusion than Feistel structures.")

evaluate()