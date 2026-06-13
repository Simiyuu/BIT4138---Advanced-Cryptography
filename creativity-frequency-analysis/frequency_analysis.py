import matplotlib.pyplot as plt
import string

def frequency_analysis(ciphertext):
    ciphertext = ciphertext.upper()
    frequency = {}
    
    for letter in string.ascii_uppercase:
        frequency[letter] = ciphertext.count(letter)
    
    total = sum(frequency.values())
    percentages = {k: (v/total)*100 for k, v in frequency.items()}
    
    print("=== Frequency Analysis Results ===")
    for letter, percent in percentages.items():
        bar = "█" * int(percent)
        print(f"{letter}: {bar} {percent:.2f}%")
    
    plt.figure(figsize=(14, 6))
    plt.bar(percentages.keys(), percentages.values(), color='red')
    plt.title('Letter Frequency Analysis - Cryptanalysis Toolkit')
    plt.xlabel('Letters')
    plt.ylabel('Frequency (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('frequency_analysis.png')
    plt.show()
    print("\nChart saved as frequency_analysis.png")

ciphertext = "FUBSWDQDOBVLV WRRONLW VHFXULWB WHVWLQJ WRRONLW"
frequency_analysis(ciphertext)