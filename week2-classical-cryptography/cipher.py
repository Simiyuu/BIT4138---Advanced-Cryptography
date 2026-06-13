def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

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

print("\n=== Cryptanalysis & Security Testing Toolkit ===")
print("1. Caesar Cipher")
print("2. Vigenère Cipher")
choice = input("Select cipher (1 or 2): ")

if choice == "1":
    message = input("Enter message: ")
    shift_input = input("Enter shift value (1-25): ")
    
    if not shift_input.isdigit():
        print("Error: Shift must be a valid number.")
    elif int(shift_input) < 1 or int(shift_input) > 25:
        print("Error: Shift must be between 1 and 25.")
    else:
        print(f"Encrypted: {caesar_cipher(message.upper(), int(shift_input))}")

elif choice == "2":
    message = input("Enter message: ")
    key = input("Enter keyword: ")
    
    if not key.isalpha():
        print("Error: Keyword must contain ONLY letters (no numbers or spaces).")
    else:
        print(f"Encrypted: {vigenere_encrypt(message.upper(), key)}")

else:
    print("Error: Invalid choice. Please restart and select 1 or 2.")