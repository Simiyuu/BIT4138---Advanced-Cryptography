def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

message = "CRYPTANALYSIS TOOLKIT"
key = "SECURITY"

encrypted = vigenere_encrypt(message, key)
print(f"Original:  {message}")
print(f"Key:       {key}")
print(f"Encrypted: {encrypted}")

decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")