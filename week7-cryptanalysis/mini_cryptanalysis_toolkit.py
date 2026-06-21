from collections import Counter

def calculate_difference(p1, p2):
    print("=== Input Difference Calculator ===")
    diff = p1 ^ p2
    print(f"Plaintext 1: {p1} (binary: {format(p1, '08b')})")
    print(f"Plaintext 2: {p2} (binary: {format(p2, '08b')})")
    print(f"XOR Difference: {diff} (binary: {format(diff, '08b')})")
    bits_different = bin(diff).count('1')
    print(f"Bits Different: {bits_different}/8")
    return diff

def frequency_analysis(data):
    print("\n=== Frequency Analysis ===")
    count = Counter(data)
    total = len(data)
    for char, freq in count.most_common():
        percentage = (freq / total) * 100
        bar = "█" * int(percentage / 2)
        print(f"{char}: {bar} {freq} ({percentage:.1f}%)")
    return count

def statistical_bias(successes, total):
    print("\n=== Statistical Bias Measurement ===")
    probability = successes / total
    expected = 0.5
    bias = abs(probability - expected)
    print(f"Observed Probability: {probability:.4f}")
    print(f"Expected Probability (Random): {expected:.4f}")
    print(f"Bias: {bias:.4f}")
    if bias > 0.05:
        print("Result: SIGNIFICANT bias detected — potential vulnerability!")
    else:
        print("Result: Bias is within normal random range — no major weakness detected.")
    return bias

def generate_report(diff, freq_data, bias):
    print("\n" + "=" * 50)
    print("AUTOMATED CRYPTANALYSIS REPORT")
    print("=" * 50)
    print(f"XOR Difference Detected: {diff}")
    print(f"Most Frequent Character: {freq_data.most_common(1)[0][0]} "
          f"({freq_data.most_common(1)[0][1]} occurrences)")
    print(f"Statistical Bias: {bias:.4f}")
    print("Toolkit successfully automated difference, frequency, and bias analysis.")

print("MINI CRYPTANALYSIS TOOLKIT")
print("=" * 50)

diff = calculate_difference(200, 201)
freq_data = frequency_analysis("ABABABABCCCCDDD")
bias = statistical_bias(75, 100)
generate_report(diff, freq_data, bias)