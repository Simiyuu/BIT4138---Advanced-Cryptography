def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

message = "CRYPTANALYSIS TOOLKIT"
encrypted = caesar_cipher(message, 3)
print(f"Original: {message}")
print(f"Encrypted: {encrypted}")


