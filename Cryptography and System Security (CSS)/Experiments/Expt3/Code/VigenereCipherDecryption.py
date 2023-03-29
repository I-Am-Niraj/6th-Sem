def decrypt_vigenere(str, key):
    numstr = [0] * 100
    numkey = [0] * 100
    numcipher = [0] * 100
    j = 0
    str = str.upper()
    for i in range(len(str)):
        numstr[i] = ord(str[i]) - ord('A')
    key = key.upper()
    i = 0
    for j in range(len(key)):
        if i >= len(str):
            break
        numkey[i] = ord(key[j]) - ord('A')
        i += 1
    while i < len(str):
        for j in range(len(key)):
            numkey[i] = ord(key[j]) - ord('A')
            i += 1
    for i in range(len(str)):
        numcipher[i] = (numstr[i] - numkey[i]) % 26
    return ''.join(chr(numcipher[i] + ord('A')) for i in range(len(str)))

str = input("Enter a string to decrypt: ")
key = input("Enter a key: ")
print("Decrypted Vigenere Cipher text is:")
print(decrypt_vigenere(str, key))
