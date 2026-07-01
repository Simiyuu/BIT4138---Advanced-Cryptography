from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

def encrypt_image_mode(input_file, mode_name):
    print(f"=== AES {mode_name} Image Encryption ===")
    
    if not os.path.exists(input_file):
        print(f"[-] Error: '{input_file}' not found.")
        return

    with open(input_file, 'rb') as f:
        file_data = bytearray(f.read())

    header = file_data[:54]
    pixel_data = bytes(file_data[54:])

    key = b'SECRET_KEY_12345' 

    padded_pixels = pad(pixel_data, AES.block_size)

    if mode_name == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_pixels = cipher.encrypt(padded_pixels)
        output_file = "encrypted_ECB.bmp"
        
    elif mode_name == "CBC":
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_pixels = cipher.encrypt(padded_pixels)
        output_file = "encrypted_CBC.bmp"

    encrypted_pixels = encrypted_pixels[:len(pixel_data)]
    
    with open(output_file, 'wb') as f:
        f.write(header + encrypted_pixels)
        
    print(f"[+] Saved {mode_name} encrypted image as '{output_file}'.\n")

target_image = "test_image.bmp" 

print("[*] Starting AES Block Mode Visualization...\n")
encrypt_image_mode(target_image, "ECB")
encrypt_image_mode(target_image, "CBC")
print("[*] Open 'encrypted_ECB.bmp' and 'encrypted_CBC.bmp' to compare the visual patterns.")