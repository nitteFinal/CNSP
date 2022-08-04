def encrypt(plaintext, key):
    cipher = ""
    for x in plaintext:
        if x.isupper():
            value = chr((ord(x)+key-65) % 26+65)
            cipher += value
        else:
            value = chr((ord(x)+key-97) % 26+97)
            cipher += value
    print(cipher)


def decrypt(cipher, key):
    plaintext = ""
    for x in cipher:
        if x.isupper():
            value = chr((ord(x)-key-65) % 26+65)
            plaintext += value
        else:
            value = chr((ord(x)-key-97) % 26+97)
            plaintext += value
    print(plaintext)


choice = int(input("Enter 1 to encrypt or 2 to decrypt"))
if choice == 1:
    plaintext = input("Enter the plain text")
    key = int(input("Enter the key"))
    encrypt(plaintext, key)

if choice == 2:
    Cipher = input("Enter the ciphertext")
    key = int(input("Enter the key"))
    decrypt(Cipher, key)
