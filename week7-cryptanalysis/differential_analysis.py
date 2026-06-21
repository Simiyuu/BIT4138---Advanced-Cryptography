def simple_cipher(plaintext, key):
    return (plaintext ^ key) % 256

def differential_analysis(p1, p2, key):
    print("=== Differential Cryptanalysis Simulation ===")
    print(f"Plaintext 1: {p1} (binary: {format(p1, '08b')})")
    print(f"Plaintext 2: {p2} (binary: {format(p2, '08b')})")

    input_diff = p1 ^ p2
    print(f"\nInput Difference (XOR): {input_diff} (binary: {format(input_diff, '08b')})")

    c1 = simple_cipher(p1, key)
    c2 = simple_cipher(p2, key)
    print(f"\nCiphertext 1: {c1} (binary: {format(c1, '08b')})")
    print(f"Ciphertext 2: {c2} (binary: {format(c2, '08b')})")

    output_diff = c1 ^ c2
    print(f"\nOutput Difference (XOR): {output_diff} (binary: {format(output_diff, '08b')})")

    print("\n=== Observation ===")
    if input_diff == output_diff:
        print("Input difference equals output difference.")
        print("This reveals a predictable XOR-based relationship —")
        print("a weakness an attacker could exploit to recover the key.")
    else:
        print("Input and output differences differ, indicating")
        print("the transformation introduces some non-linearity.")

p1 = 200
p2 = 201
key = 77
differential_analysis(p1, p2, key)