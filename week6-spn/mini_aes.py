SBOX = {0: 14, 1: 4, 2: 13, 3: 1,
        4: 2, 5: 15, 6: 11, 7: 8,
        8: 3, 9: 10, 10: 6, 11: 12,
        12: 5, 13: 9, 14: 0, 15: 7}

SBOX_INV = {v: k for k, v in SBOX.items()}

PERMUTATION = [3, 0, 2, 1]
PERMUTATION_INV = [1, 3, 0, 2]

def substitute(value, box):
    return box[value % 16]

def permute(bits, perm):
    result = ['0'] * 4
    for i, pos in enumerate(perm):
        result[pos] = bits[i]
    return ''.join(result)

def generate_round_keys(master_key, rounds):
    keys = []
    for i in range(rounds):
        keys.append((master_key ^ (i * 31)) % 16)
    return keys

def mini_aes_encrypt(plaintext, master_key, rounds=4):
    print("=== Mini AES-Inspired Encryption ===")
    print(f"Plaintext:   {plaintext} (binary: {format(plaintext % 16, '04b')})")
    print(f"Master Key:  {master_key}")
    print(f"Rounds:      {rounds}")
    print("-" * 50)

    round_keys = generate_round_keys(master_key, rounds)
    state = plaintext

    for r in range(rounds):
        print(f"\n[ROUND {r+1}]")
        state = state ^ round_keys[r]
        print(f"  Key Mixing:    {state} (binary: {format(state % 16, '04b')})")

        state = substitute(state, SBOX)
        print(f"  SubBytes:      {state} (binary: {format(state, '04b')})")

        bits = format(state, '04b')
        permuted = permute(bits, PERMUTATION)
        state = int(permuted, 2)
        print(f"  ShiftRows:     {state} (binary: {permuted})")

    print(f"\nFinal Ciphertext: {state} (binary: {format(state, '04b')})")
    return state, round_keys

def mini_aes_decrypt(ciphertext, round_keys, rounds=4):
    print("\n=== Mini AES-Inspired Decryption ===")
    print(f"Ciphertext: {ciphertext} (binary: {format(ciphertext, '04b')})")
    print("-" * 50)

    state = ciphertext

    for r in range(rounds - 1, -1, -1):
        print(f"\n[ROUND {r+1} INVERSE]")
        bits = format(state, '04b')
        permuted = permute(bits, PERMUTATION_INV)
        state = int(permuted, 2)
        print(f"  Inverse ShiftRows:  {state} (binary: {permuted})")

        state = substitute(state, SBOX_INV)
        print(f"  Inverse SubBytes:   {state} (binary: {format(state, '04b')})")

        state = state ^ round_keys[r]
        print(f"  Key Mixing:         {state} (binary: {format(state % 16, '04b')})")

    print(f"\nDecrypted Plaintext: {state} (binary: {format(state, '04b')})")
    return state

def security_analysis(plaintext, key):
    print("\n=== Security Analysis ===")
    test_cases = [(plaintext, key), (plaintext + 1, key), (plaintext, key + 1)]

    print(f"{'Plaintext':<15} {'Key':<10} {'Ciphertext':<15} {'Binary'}")
    print("-" * 55)

    results = []
    for p, k in test_cases:
        rk = generate_round_keys(k, 4)
        state = p
        for r in range(4):
            state = state ^ rk[r]
            state = substitute(state, SBOX)
            bits = format(state, '04b')
            state = int(permute(bits, PERMUTATION), 2)
        results.append(state)
        print(f"{p:<15} {k:<10} {state:<15} {format(state, '04b')}")

    print("\nAvalanche Check:")
    print(f"Plaintext change  → Ciphertext difference: {results[0] ^ results[1]} (binary: {format(results[0] ^ results[1], '04b')})")
    print(f"Key change        → Ciphertext difference: {results[0] ^ results[2]} (binary: {format(results[0] ^ results[2], '04b')})")

# Run full simulation
plaintext = 9
master_key = 5

ciphertext, round_keys = mini_aes_encrypt(plaintext, master_key, rounds=4)
decrypted = mini_aes_decrypt(ciphertext, round_keys, rounds=4)

print("\n=== Verification ===")
print(f"Original Plaintext:  {plaintext}")
print(f"Decrypted Plaintext: {decrypted}")
print(f"Match: {'✓ SUCCESS' if plaintext == decrypted else '✗ FAILED'}")

security_analysis(plaintext, master_key)