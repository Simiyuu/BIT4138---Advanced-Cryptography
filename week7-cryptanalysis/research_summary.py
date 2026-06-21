def print_section(title, points):
    print(f"\n=== {title} ===")
    for point in points:
        print(f"- {point}")

print("BLOCK CIPHER CRYPTANALYSIS RESEARCH SUMMARY")
print("=" * 50)

print_section("Differential Cryptanalysis", [
    "Introduced by Biham and Shamir in the late 1980s",
    "Studies how differences in plaintext affect differences in ciphertext",
    "Effective against ciphers with weak S-Boxes",
    "Used to break early versions of DES-like ciphers",
    "Real-world example: helped evaluate DES security standards"
])

print_section("Linear Cryptanalysis", [
    "Introduced by Mitsuru Matsui in 1993",
    "Uses linear approximations between plaintext, ciphertext, and key bits",
    "Relies on large amounts of known plaintext-ciphertext pairs",
    "Exploits statistical bias rather than exact equations",
    "Real-world example: successfully attacked full DES with 2^43 known plaintexts"
])

print_section("Algebraic Attacks", [
    "Expresses encryption as a system of mathematical equations",
    "Attempts to solve those equations to recover the secret key",
    "Faster than brute force when the cipher has low non-linearity",
    "Exploits weak or predictable S-Box structures",
    "Real-world example: used to analyze simplified AES variants"
])

print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)
print("All three attacks exploit predictable mathematical relationships.")
print("Modern ciphers like AES defend against them using strong S-Boxes,")
print("multiple rounds, and high non-linearity to resist these techniques.")