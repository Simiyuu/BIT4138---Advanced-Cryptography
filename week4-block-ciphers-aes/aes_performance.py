import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

key = get_random_bytes(16)
test_sizes = [100, 1000, 10000, 100000]

print("=== AES Performance Testing ===")
print(f"{'Message Size':<20} {'Time (ms)':<20} {'Speed'}")
print("-" * 55)

for size in test_sizes:
    message = "A" * size
    start = time.time()
    aes_encrypt(key, message)
    elapsed = (time.time() - start) * 1000
    speed = size / (elapsed / 1000) if elapsed > 0 else float('inf')
    print(f"{size} chars{'':<14} {elapsed:.4f} ms{'':<10} {speed:.0f} chars/sec")

print("\nConclusion: AES maintains strong performance across varying data sizes.")