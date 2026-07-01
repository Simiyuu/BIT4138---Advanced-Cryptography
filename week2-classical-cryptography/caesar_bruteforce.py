def decrypt_caesar(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

def brute_force_caesar(ciphertext):
    print("=== Automated Caesar Cipher Brute-Forcer ===")
    print(f"Target Ciphertext: {ciphertext}\n")
    print("-" * 50)
    

    for shift in range(1, 26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        
        if "CRYPTANALYSIS" in decrypted_text:
            print(f"[!] Shift {shift:02d}: {decrypted_text} <--- POSSIBLE MATCH")
        else:
            print(f"[-] Shift {shift:02d}: {decrypted_text}")
            
    print("-" * 50)
    print("[*] Brute-force complete. Review the output for readable text.")

target_ciphertext = "FUBSWDQDOBVLV WRRONLW"

brute_force_caesar(target_ciphertext)