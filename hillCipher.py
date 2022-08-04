import numpy as np

plainText = input("Enter the plain text").lower()
key = input("Enter the key").lower()
key = np.array([ord(b)-97 for b in key])

if(len(key) == 4):
    size = 2
    keyMatrix = key.reshape(2, 2)
if (len(key) == 9):
    size = 3
    keyMatrix = key.reshape(3, 3)

while(len(plainText) % size != 0):
    plainText += 'x'

plainText = np.array([ord(a)-97 for a in plainText])
plainTextMatrix = np.array_split(plainText, len(plainText)/size)
encryptedText = []
print("Encrypted Value:", end=" ")
for a in plainTextMatrix:
    a = a.reshape(size, 1)
    product = np.dot(keyMatrix, a) % 26
    for a in np.nditer(product):
        encryptedText.append(a)
        print(chr(a+97), end="")
print()
adjointMatrix = np.linalg.inv(keyMatrix)
determinant = round(np.linalg.det(keyMatrix))
adjointMatrix = adjointMatrix*determinant

np.where(adjointMatrix < 0, adjointMatrix+26, adjointMatrix)

inverseDivisor = 1

while((determinant*inverseDivisor) % 26 != 1):
    inverseDivisor += 1
print(inverseDivisor)
adjointMatrix = (inverseDivisor*adjointMatrix) % 26
print(adjointMatrix)
encryptedText = np.array(encryptedText)
encryptedMatrix = np.array_split(encryptedText, len(encryptedText)/size)
print("Decrypted Text:", end=" ")
for a in encryptedMatrix:
    a = a.reshape(size, 1)
    product = np.round_(np.dot(adjointMatrix, a)).astype(int)
    product = product % 26
    for a in np.nditer(product):
        print(chr(a+97), end="")
