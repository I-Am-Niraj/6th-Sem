def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            key_amount = ord(char) + key
            if char.isupper():
                if key_amount > ord("Z"):
                    key_amount -= 26
                elif key_amount < ord("A"):
                    key_amount += 26
                ciphertext += chr(key_amount)
            elif char.islower():
                if key_amount > ord("z"):
                    key_amount -= 26
                elif key_amount < ord("a"):
                    key_amount += 26
                ciphertext += chr(key_amount)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            key_amount = ord(char) - key
            if char.isupper():
                if key_amount > ord("Z"):
                    key_amount -= 26
                elif key_amount < ord("A"):
                    key_amount += 26
                plaintext += chr(key_amount)
            elif char.islower():
                if key_amount > ord("z"):
                    key_amount -= 26
                elif key_amount < ord("a"):
                    key_amount += 26
                plaintext += chr(key_amount)
        else:
            plaintext += char
    return plaintext

plaintext = input("Enter Plain Text: ")
key = int(input("Enter key for encryption: "))
ciphertext = encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print("Decrypted plaintext: ", decrypted_plaintext)
