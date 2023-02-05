import time
import string
import os

#clear terminal
def clear():
    os.system("cls")

#pause program for <duration> seconds
def pause(duration):
    time.sleep(duration)

#visual effect for calculating plaintext/ciphertext
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

#encrypts plaintext, shifting alphabet by <key> letters right
def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    #loops through all characters in plaintext
    for char in plaintext:
        #shifts index by <key> to the right
        ciphercharindex = alphabet.index(char) + int(key)
        if(ciphercharindex >= len(alphabet)):
            ciphercharindex -= len(alphabet)
        cipherchar = alphabet[ciphercharindex]
        #adds cipherchar to ciphertext
        ciphertext = ciphertext + cipherchar
    clear()
    #visuals to make it look nice
    print("Plaintext:\t" + plaintext)
    print("Key:\t" + str(key))
    pause(3)
    loadingBar("e")
    print("Ciphertext:\t" + ciphertext)
    print("Key:\t" + str(key) + "\n")
    input("Press enter to continue...")
    clear()


#decrypts ciphertext by shifting alphabet <key> letters left
def decrypt(ciphertext, key, alphabet):
    plaintext = ""
    #iterates through all characters in ciphertext
    for char in ciphertext:
        #
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

#main function, takes user input to choose mode
def main():
    clear()
    #list of available characters
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)
    #print(alphabet)
    print("Welcome to Caesar Cipher!")
    mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
    #user will continue to be prompted until the enter "exit" to quit
    while(mode != "exit"):
        #if user enters "e", proceeds with encryption prompts
        if mode == "e":
            clear()
            plaintext = input("Enter the plaintext you want to encrypt:\t")
            key = input("Enter the number of letter shift:\t")
            encrypt(plaintext, key, alphabet)
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
        #if user enters "d", proceeds with decryption prompts
        elif mode == "d":
            clear()
            ciphertext = input("Enter the ciphertext you wish to decrypt:\t")
            key = input("Enter the letter shift used to encrypt the message:\t")
            decrypt(ciphertext, key, alphabet)
            
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
        #if user inputs something other, they will be corrected
        else:
            clear()
            print("Please enter a valid command...")
            pause(3)
            clear
            mode = input("Would you like to Encrypt, Decrypt, or exit (e / d / exit):\t")
    #goodbye message for when they quit
    print("Goodbye!")
        


main()

