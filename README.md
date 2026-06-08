# Cryptanalysis & Security Testing Toolkit
### BIT4138: Advanced Cryptography
**Student:** Chandler Matere Simiyu
**Admission Number:** BSCCS/2024/58571 
**GitHub:** https://github.com/Simiyuu/cryptanalysis-toolkit


---

## Project Overview
The Cryptanalysis & Security Testing Toolkit is a Python-based application developed as part of the BIT4138 Advanced Cryptography unit. The toolkit goes beyond basic encryption by analyzing and exposing weaknesses in cipher implementations. It covers classical ciphers, stream ciphers, block ciphers, asymmetric encryption and cryptanalysis techniques.

---

## Project Structure

cryptanalysis-toolkit/
├── caesar.py               # Week 1 - Caesar Cipher Implementation
├── vigenere.py             # Week 2 - Vigenère Cipher Implementation
├── cipher_menu.py          # Week 2 - User Input Validation Interface
├── cipher_test.py          # Week 2 - Cipher Testing Suite
├── lfsr.py                 # Week 3 - LFSR Pseudorandom Generator
├── randomness_test.py      # Week 3 - Statistical Randomness Testing
├── rc4.py                  # Week 3 - RC4 Stream Cipher Simulation
├── performance_test.py     # Week 3 - Encryption Performance Testing
├── aes_encrypt.py          # Week 4 - AES Encryption Implementation
├── key_generation.py       # Week 4 - AES Key Generation
├── file_encrypt.py         # Week 4 - File Encryption Demonstration
├── file_decrypt.py         # Week 4 - File Decryption Demonstration
├── aes_performance.py      # Week 4 - AES Performance Testing
├── rsa_keygen.py           # Week 5 - RSA Key Pair Generation
├── rsa_encrypt.py          # Week 5 - RSA Public Key Encryption
├── rsa_decrypt.py          # Week 5 - RSA Private Key Decryption
├── rsa_transmission.py     # Week 5 - Secure Message Transmission
├── rsa_test.py             # Week 5 - RSA Testing and Validation
├── frequency_analysis.py   # Creativity - Frequency Analysis Visualizer
├── secret.txt              # Sample file for encryption demonstration
├── public_key.pem          # Generated RSA Public Key
├── private_key.pem         # Generated RSA Private Key
└── README.md               # Project Documentation

---

## Weekly Breakdown

### Week 1 — Environment Setup
Installation and configuration of Python, VS Code, PyCryptodome, OpenSSL and GitHub repository initialization.

### Week 2 — Classical Cryptography
Implementation of Caesar and Vigenère cipher modules with user input validation and cipher testing suite.

### Week 3 — Stream Ciphers & Randomness Testing
LFSR pseudorandom generator and RC4 stream cipher implemented. Frequency, Runs and Mean statistical tests performed to validate randomness quality.

### Week 4 — Block Ciphers & AES
AES encryption and decryption implemented using CBC mode with random IV generation, PKCS padding and secure key generation. File encryption demonstrated.

### Week 5 — Asymmetric Encryption & RSA
RSA 2048-bit key pair generation implemented with public key encryption and private key decryption. Secure message transmission simulated and validated through a full testing suite.

### Creativity — Frequency Analysis Visualizer
A real-world cryptanalysis technique implemented using Matplotlib to visualize letter frequency distributions in ciphertext, exposing weaknesses in classical cipher implementations.

---

## Technologies Used
| Tool | Purpose |
|------|---------|
| Python 3.14.3 | Core programming language |
| PyCryptodome | Cryptographic implementations |
| Matplotlib | Frequency analysis visualization |
| OpenSSL | Key and certificate generation |
| Git & GitHub | Version control and repository hosting |
| VS Code | Development environment |

---

## How To Run
1. Clone the repository:
git clone https://github.com/Simiyuu/cryptanalysis-toolkit.git
2. Install dependencies:
pip install pycryptodome matplotlib
3. Run any module:
python caesar.py
python rc4.py
python aes_encrypt.py
python rsa_test.py
python frequency_analysis.py

---

## Academic Integrity
This toolkit was developed as part of BIT4138 Advanced Cryptography coursework. All implementations are original work developed for educational purposes.

---
*BIT4138 — Advanced Cryptography | Mount Kenya University