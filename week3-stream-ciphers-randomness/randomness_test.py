def frequency_test(sequence):
    ones = sequence.count(1)
    zeros = sequence.count(0)
    total = len(sequence)
    print("=== Frequency Test ===")
    print(f"Ones: {ones} ({(ones/total)*100:.1f}%)")
    print(f"Zeros: {zeros} ({(zeros/total)*100:.1f}%)")
    print(f"Result: {'PASS - Balanced' if abs(ones-zeros) <= total*0.1 else 'FAIL - Unbalanced'}")

def runs_test(sequence):
    runs = 1
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            runs += 1
    print("\n=== Runs Test ===")
    print(f"Total Runs: {runs}")
    print(f"Result: {'PASS - Good randomness' if runs > len(sequence)//4 else 'FAIL - Poor randomness'}")

def mean_test(sequence):
    mean = sum(sequence) / len(sequence)
    print("\n=== Mean Test ===")
    print(f"Mean: {mean:.4f}")
    print(f"Result: {'PASS - Close to 0.5' if 0.4 <= mean <= 0.6 else 'FAIL - Biased'}")

sequence = [1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0]
frequency_test(sequence)
runs_test(sequence)
mean_test(sequence)