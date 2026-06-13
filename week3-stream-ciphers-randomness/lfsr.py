def lfsr(seed, taps, length):
    state = seed
    sequence = []
    for _ in range(length):
        feedback = 0
        for tap in taps:
            feedback ^= (state >> tap) & 1
        sequence.append(state & 1)
        state = (state >> 1) | (feedback << (len(bin(seed)) - 3))
    return sequence

seed = 0b1011
taps = [3, 1]
sequence = lfsr(seed, taps, 20)
print("=== LFSR Generator ===")
print(f"Seed: {bin(seed)}")
print(f"Taps: {taps}")
print(f"Generated Sequence: {sequence}")