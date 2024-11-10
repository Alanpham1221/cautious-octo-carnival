
import binascii

# Hexadecimal string
hex_string = "YOUR STRING OF CHARACTERS"

# Convert hex string to ASCII
ascii_string = binascii.unhexlify(hex_string.replace(" ", "")).decode('utf-8')

# Load the wordlist from file
wordlist_path = r'YOUR PATH TO FILE'
with open(wordlist_path, 'r', encoding='latin-1') as f:
    wordlist = f.readlines()
wordlist = [word.strip() for word in wordlist]

# Brute force heart
found = False
for word in wordlist:
    print(f"Attempting: {word}")
    if word == ascii_string:
        print(f"Match found: {word}")
        found = True
        break

if not found:
    print("Nothing")
