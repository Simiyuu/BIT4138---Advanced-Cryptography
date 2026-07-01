def explain_concepts():
    print("=== Class Exercise 1: Understanding Asymmetric Cryptography ===\n")

    concepts = {
        "Public Key": "A key that can be shared openly with anyone. Used to encrypt messages or verify digital signatures.",
        "Private Key": "A secret key known only to its owner. Used to decrypt messages or create digital signatures.",
        "Symmetric Encryption": "Uses one single key for both encryption and decryption. Faster but requires secure key distribution.",
        "Asymmetric Encryp week8tion": "Uses a mathematically linked key pair (public and private). Slower but solves the key distribution problem."
    }

    for term, definition in concepts.items():
        print(f"{term}:")
        print(f"  {definition}\n")

    print("=== Class Exercise 2: Complexity and Cryptography ===\n")
    print("Why computationally hard problems are important in cryptography:")
    print("Cryptographic security depends on problems that are easy to compute")
    print("in one direction but extremely difficult to reverse without the key.\n")

    print("Examples of hard problems used in cryptography:")
    examples = [
        "Integer Factorization (used in RSA) - multiplying two large primes is easy, factoring the product back is hard.",
        "Discrete Logarithm Problem (used in Diffie-Hellman) - computing g^a mod p is easy, finding 'a' is hard.",
        "Elliptic Curve Discrete Logarithm Problem (used in ECC) - similar difficulty but with smaller key sizes."
    ]
    for i, ex in enumerate(examples, 1):
        print(f"{i}. {ex}")

explain_concepts()