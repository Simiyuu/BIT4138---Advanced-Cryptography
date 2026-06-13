def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

test_cases = [
    ("HELLO", 3),
    ("SECURITY", 7),
    ("CRYPTANALYSIS", 13),
]

print("=== Caesar Cipher Test Results ===")
for message, shift in test_cases:
    encrypted = caesar_cipher(message, shift)
    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Original: {message} | Shift: {shift} | Encrypted: {encrypted} | Decrypted: {decrypted}")