from collections import Counter

def simple_cipher(plaintext, key):
    return (plaintext ^ key) % 256

def avalanche_test(p1, p2, key):
    print("=== Avalanche Effect Testing ===")
    c1 = simple_cipher(p1, key)
    c2 = simple_cipher(p2, key)
    diff = c1 ^ c2
    bits_changed = bin(diff).count('1')
    percentage = (bits_changed / 8) * 100
    print(f"Plaintext 1: {p1} | Plaintext 2: {p2}")
    print(f"Ciphertext 1: {c1} | Ciphertext 2: {c2}")
    print(f"Bits Changed: {bits_changed}/8 ({percentage:.1f}%)")
    if percentage >= 50:
        print("Result: STRONG avalanche effect detected.\n")
    else:
        print("Result: WEAK avalanche effect — cipher may be vulnerable.\n")
    return bits_changed

def difference_analysis(p1, p2):
    print("=== Difference Analysis ===")
    diff = p1 ^ p2
    print(f"Input Difference: {diff} (binary: {format(diff, '08b')})")
    print(f"Hamming Weight: {bin(diff).count('1')} bits\n")
    return diff

def frequency_distribution(data):
    print("=== Frequency Distribution ===")
    count = Counter(data)
    for char, freq in count.most_common():
        bar = "█" * freq
        print(f"{char}: {bar} ({freq})")
    print()
    return count

def statistical_report(avalanche_bits, diff, freq_data):
    print("=" * 50)
    print("BLOCK CIPHER SECURITY ANALYSIS REPORT")
    print("=" * 50)
    print(f"Avalanche Bits Changed:     {avalanche_bits}/8")
    print(f"Input Difference (Hamming): {bin(diff).count('1')} bits")
    print(f"Most Frequent Symbol:       {freq_data.most_common(1)[0][0]}")
    print(f"Unique Symbols Found:       {len(freq_data)}")

    security_score = (avalanche_bits / 8) * 100
    print(f"\nOverall Security Score: {security_score:.1f}%")
    if security_score >= 50:
        print("VERDICT: Cipher demonstrates acceptable diffusion properties.")
    else:
        print("VERDICT: Cipher shows weak diffusion — vulnerable to analysis.")
    print("=" * 50)

print("BLOCK CIPHER SECURITY ANALYZER")
print("=" * 50)
print()

avalanche_bits = avalanche_test(200, 201, 77)
diff = difference_analysis(200, 201)
freq_data = frequency_distribution("ABABABABCCCCDDD")
statistical_report(avalanche_bits, diff, freq_data)