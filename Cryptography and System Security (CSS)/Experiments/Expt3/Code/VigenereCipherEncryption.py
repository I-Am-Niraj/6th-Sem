def encrypt(str, key):
    numstr = [0] * 100
    numkey = [0] * 100
    numcipher = [0] * 100

    print("Entered string is: " + str)
    for i in range(len(str)):
        numstr[i] = ord(str[i]) - ord('A')
    j = 0
    for i in range(len(str)):
        if j >= len(key):
            j = 0
        numkey[i] = ord(key[j]) - ord('A')
        j += 1
    for i in range(len(str)):
        numcipher[i] = (numstr[i] + numkey[i]) % 26

    print("Vigenere Cipher text is")
    for i in range(len(str)):
        print(chr(numcipher[i] + ord('A')), end='')
    print("")

str = input("Enter a string: ")
str = str.upper()
key = input("Enter a key: ")
key = key.upper()
encrypt(str, key)
