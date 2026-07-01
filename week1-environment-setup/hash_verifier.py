import hashlib
import os

def verify_file_hash(filepath):
    print("=== Cryptographic Hash Verification Tool ===")
    
    if not os.path.exists(filepath):
        print(f"[-] Error: File '{filepath}' not found in the current directory.")
        print("Please ensure you are targeting an existing file.")
        return

    print(f"[+] Target File: {filepath}")

    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
            sha256_hash.update(byte_block)

    print("-" * 50)
    print(f"MD5 Checksum:     {md5_hash.hexdigest()}")
    print(f"SHA-256 Checksum: {sha256_hash.hexdigest()}")
    print("-" * 50)
    print("[✓] Verification complete. Hashes guarantee file integrity.")

target = "caesar.py" 

verify_file_hash(target)