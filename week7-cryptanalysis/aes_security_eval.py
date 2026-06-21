def print_section(title, points):
    print(f"\n=== {title} ===")
    for point in points:
        print(f"- {point}")

print("AES SECURITY EVALUATION REPORT")
print("=" * 50)

print_section("Resistance to Differential Cryptanalysis", [
    "AES uses a highly non-linear S-Box (max differential probability 4/256)",
    "10-14 rounds ensure differences are spread throughout the entire block",
    "No effective differential characteristic has been found for full AES",
    "The Wide Trail Strategy guarantees a minimum number of active S-Boxes per round"
])

print_section("Resistance to Linear Cryptanalysis", [
    "AES S-Box achieves a non-linearity score of 112 out of 128",
    "Strong diffusion through ShiftRows and MixColumns operations",
    "Best known linear attacks require more plaintext than is practically available",
    "No practical linear attack exists against full 10-round AES"
])

print_section("Modern Research Findings", [
    "Best known attacks on AES are only marginally faster than brute force",
    "Related-key attacks exist for AES-256 but require unrealistic conditions",
    "NIST continues to recommend AES as the global encryption standard",
    "No practical attack has broken full AES encryption to date"
])

print("\n" + "=" * 50)
print("CONCLUSION")
print("=" * 50)
print("AES remains secure due to its strong S-Box design, sufficient")
print("rounds, and excellent diffusion properties. It successfully")
print("resists both differential and linear cryptanalysis, making it")
print("the trusted global standard for symmetric encryption.")