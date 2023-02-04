import time
import string
import os

def clear():
    os.system("cls")

def pause(duration):
    time.sleep(duration)

def loadingBar(mode):
    periodCount = 1
    if mode == "e":
        for i in range(9):
            clear()
            print("Calculating ciphertext" + "."*periodCount)
            pause(1)
            periodCount += 1
            if periodCount == 4:
                periodCount = 1
    elif mode == "d":
        for i in range(9):
            clear()
            print("Calculating plaintext" + "."*periodCount)
            pause(1)
            periodCount += 1
            if periodCount == 4:
                periodCount = 1
    clear()

def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    for char in plaintext:
        ciphercharindex = alphabet.index(char) + int(key)
        if(ciphercharindex >= len(alphabet)):
            ciphercharindex -= len(alphabet)
        cipherchar = alphabet[ciphercharindex]
        ciphertext = ciphertext + cipherchar
    clear()
    print("Plaintext:\t" + plaintext)
    print("Key:\t" + str(key))
    pause(3)
    loadingBar("e")
    print("Ciphertext:\t" + ciphertext)
    print("Key:\t" + str(key) + "\n")
    input("Press enter to continue...")
    clear()


def decrypt(ciphertext, key, alphabet):
    plaintext = ""
    for char in ciphertext:
        plaintextcharindex = alphabet.index(char) - int(key)
        if(plaintextcharindex < 0):
            plaintextcharindex += len(alphabet)
        plaintextchar = alphabet[plaintextcharindex]
        plaintext = plaintext + plaintextchar 
    clear()
    print("Ciphertext:\t" + ciphertext)
    print("Key:\t" + str(key))
    pause(3)
    loadingBar("d")
    print("Plaintext:\t" + plaintext)
    print("Key:\t" + str(key) + "\n")
    input("Press enter to continue...")
    clear()

def main():
    clear()
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)
    #print(alphabet)
    print("Welcome to Caesar Cipher!")
    mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
    while(mode != "exit"):
        if mode == "e":
            clear()
            plaintext = input("Enter the plaintext you want to encrypt:\t")
            key = input("Enter the number of letter shift:\t")
            encrypt(plaintext, key, alphabet)
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
        elif mode == "d":
            clear()
            ciphertext = input("Enter the ciphertext you wish to decrypt:\t")
            key = input("Enter the letter shift used to encrypt the message:\t")
            decrypt(ciphertext, key, alphabet)
            
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
        else:
            clear()
            print("Please enter a valid command...")
            pause(3)
            clear
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
    print("Goodbye!")
        


main()

