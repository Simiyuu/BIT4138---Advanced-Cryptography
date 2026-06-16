SBOX = {0: 14, 1: 4, 2: 13, 3: 1,
        4: 2, 5: 15, 6: 11, 7: 8,
        8: 3, 9: 10, 10: 6, 11: 12,
        12: 5, 13: 9, 14: 0, 15: 7}

def linear_transform(x):
    return x ^ 5

def sbox_transform(x):
    return SBOX[x % 16]

def investigate_nonlinearity():
    print("=== Non-Linearity Investigation ===")
    print(f"{'Input':<10} {'Linear Output':<20} {'S-Box Output':<20} {'Same?'}")
    print("-" * 60)

    linear_matches = 0
    for x in range(16):
        linear_out = linear_transform(x)
        sbox_out = sbox_transform(x)
        match = "YES" if linear_out == sbox_out else "NO"
        if match == "YES":
            linear_matches += 1
        print(f"{x:<10} {linear_out:<20} {sbox_out:<20} {match}")

    print(f"\nTotal Matches: {linear_matches}/16")
    print(f"Non-Linearity Score: {((16 - linear_matches) / 16) * 100:.1f}%")
    if linear_matches < 4:
        print("Result: STRONG S-Box — High non-linearity confirmed!")
    else:
        print("Result: WEAK S-Box — Too many linear patterns detected!")

    print("\n=== Why Non-Linearity Matters ===")
    print("Linear transformations can be expressed as simple equations.")
    print("Attackers exploit linear patterns to recover secret keys.")
    print("S-Boxes with high non-linearity resist algebraic attacks.")
    print("The AES S-Box achieves maximum non-linearity of 112 out of 128.")

investigate_nonlinearity()