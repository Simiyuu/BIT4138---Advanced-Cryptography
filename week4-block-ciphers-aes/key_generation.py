from Crypto.Random import get_random_bytes
import binascii

print("=== AES Key Generation Process ===")

key_128 = get_random_bytes(16)
key_192 = get_random_bytes(24)
key_256 = get_random_bytes(32)

print(f"128-bit Key: {binascii.hexlify(key_128).decode()}")
print(f"192-bit Key: {binascii.hexlify(key_192).decode()}")
print(f"256-bit Key: {binascii.hexlify(key_256).decode()}")
print("\nKey lengths:")
print(f"128-bit: {len(key_128)*8} bits")
print(f"192-bit: {len(key_192)*8} bits")
print(f"256-bit: {len(key_256)*8} bits")
print("\nConclusion: Longer keys provide stronger encryption security.")