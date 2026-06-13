from Crypto.PublicKey import RSA

def generate_rsa_keys():
    print("=== RSA Key Pair Generation ===")
    key = RSA.generate(2048)
    
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)
    
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)
    
    print("Key Size: 2048 bits")
    print("Public Key saved as: public_key.pem")
    print("Private Key saved as: private_key.pem")
    print(f"\nPublic Key Preview:\n{public_key.decode()[:200]}...")
    print(f"\nPrivate Key Preview:\n{private_key.decode()[:200]}...")
    print("\nKey pair generated and saved successfully!")

generate_rsa_keys()