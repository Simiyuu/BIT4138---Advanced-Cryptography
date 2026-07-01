import matplotlib.pyplot as plt

SBOX = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
PERM = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

def apply_sbox(val16):
    out = 0
    for i in range(4):
        nibble = (val16 >> (i * 4)) & 0xF
        sub = SBOX[nibble]
        out |= (sub << (i * 4))
    return out

def apply_perm(val16):
    out = 0
    for i in range(16):
        bit = (val16 >> i) & 1
        out |= (bit << PERM[i])
    return out

def spn_encrypt_simulation(val16):
    v = apply_sbox(val16)
    v = apply_perm(v)
    v = apply_sbox(v)
    v = apply_perm(v)
    return v

def hamming_weight(n):
    return bin(n).count('1')

def analyze_avalanche():
    print("=== S-Box Avalanche Effect Grapher ===")
    
    base_input = 0xAAAA 
    base_output = spn_encrypt_simulation(base_input)
    
    bit_labels = []
    distances = []
    
    print(f"Base Input:  {bin(base_input)[2:].zfill(16)}")
    print(f"Base Output: {bin(base_output)[2:].zfill(16)}\n")
    print("Testing 1-bit flips...")
    
    for i in range(16):
        flipped_input = base_input ^ (1 << i)
        flipped_output = spn_encrypt_simulation(flipped_input)
        
        diff = base_output ^ flipped_output
        distance = hamming_weight(diff)
        
        bit_labels.append(f"Bit {i}")
        distances.append(distance)
        
        print(f"[*] Flipped Input Bit {i:02d} -> Changed Output Bits: {distance}")

    plt.figure(figsize=(10, 6))
    plt.bar(bit_labels, distances, color='purple')
    
    plt.axhline(y=8, color='red', linestyle='--', label='Ideal Avalanche (50% / 8 bits)')
    
    plt.title('SPN Avalanche Effect: Output Bit Changes per Input Bit Flip')
    plt.xlabel('Flipped Input Bit')
    plt.ylabel('Number of Output Bits Changed')
    plt.ylim(0, 16)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('avalanche_effect.png')
    print("\n[+] Graph saved as 'avalanche_effect.png'.")
    plt.show()

analyze_avalanche()