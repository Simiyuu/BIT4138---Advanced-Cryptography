SBOX = {0: 14, 1: 4, 2: 13, 3: 1,
        4: 2, 5: 15, 6: 11, 7: 8,
        8: 3, 9: 10, 10: 6, 11: 12,
        12: 5, 13: 9, 14: 0, 15: 7}

PERMUTATION = [3, 0, 2, 1]

def substitute(value):
    return SBOX[value % 16]

def permute(bits):
    result = ['0'] * 4
    for i, pos in enumerate(PERMUTATION):
        result[pos] = bits[i]
    return ''.join(result)

def generate_round_keys(master_key, rounds):
    keys = []
    for i in range(rounds):
        round_key = (master_key ^ (i * 31)) % 16
        keys.append(round_key)
    return keys

def spn_multi_round(plaintext, master_key, rounds=4):
    round_keys = generate_round_keys(master_key, rounds)
    state = plaintext

    print(f"Master Key: {master_key} | Rounds: {rounds}")
    print(f"Round Keys: {round_keys}")
    print(f"\nInitial State: {state} (binary: {format(state, '04b')})")
    print("-" * 50)

    for r in range(rounds):
        state = state ^ round_keys[r]
        print(f"Round {r+1} - After Key Mix:      {state} (binary: {format(state % 16, '04b')})")

        state = substitute(state)
        print(f"Round {r+1} - After Substitution: {state} (binary: {format(state, '04b')})")

        bits = format(state, '04b')
        permuted = permute(bits)
        state = int(permuted, 2)
        print(f"Round {r+1} - After Permutation:  {state} (binary: {permuted})")
        print("-" * 50)

    return state

def avalanche_test(plaintext1, plaintext2, key):
    print("\n=== Avalanche Effect Test ===")
    print(f"Plaintext 1: {plaintext1} (binary: {format(plaintext1, '04b')})")
    print(f"Plaintext 2: {plaintext2} (binary: {format(plaintext2, '04b')})")
    print(f"Input Difference: {plaintext1 ^ plaintext2} (binary: {format(plaintext1 ^ plaintext2, '04b')})")

    cipher1 = spn_multi_round(plaintext1, key, rounds=4)
    cipher2 = spn_multi_round(plaintext2, key, rounds=4)

    diff = cipher1 ^ cipher2
    bits_changed = bin(diff).count('1')

    print(f"\nCiphertext 1: {cipher1} (binary: {format(cipher1, '04b')})")
    print(f"Ciphertext 2: {cipher2} (binary: {format(cipher2, '04b')})")
    print(f"Output Difference: {diff} (binary: {format(diff, '04b')})")
    print(f"Bits Changed: {bits_changed}/4")

    if bits_changed >= 2:
        print("Avalanche Result: STRONG — Small input change caused significant output change!")
    else:
        print("Avalanche Result: WEAK — Input change did not propagate sufficiently!")

print("=== Advanced Multi-Round SPN Encryption ===")
result = spn_multi_round(9, 5, rounds=4)
print(f"\nFinal Ciphertext: {result}")

avalanche_test(9, 8, 5)