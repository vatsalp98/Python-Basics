# Encryption/Decryption
# Description: Encrypt plaintext and decrypt ciphertext using my own algorithm
# Author: Vatsal Parmar
# Date: 5th June 2019

# function encrypt(add the key to the msg)
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

#function decrypt(we substract the key from the encrypted msg to get the original msg)
def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)



notFinished = True;
while notFinished :
	plainText = input("Please, enter a message to encrypt or S to stop: ")
# the key used to substract from the message to encrypt it
	key = 'This_is_my_awsome_secret_key'
	if plainText != 'S' and plainText != 's' :
# Call the encrypt function with plainText
# The encrypt function returns ciphertext
		print("\tLet's encrypt your message ... ")
		cipherText = encrypt(key, plainText)
# Print the ciphertext
		print("\t'{}' becomes '{}'.".format(plainText, cipherText))
# Call the decrypt function with ciphertext
# The decrypt function returnsplainText
		print("\tLet's decrypt your encrypted message ... ")
		plainText = decrypt(key, cipherText)
# Print the ciphertext and plainText
		print("\t'{}' becomes '{}'.".format(cipherText, plainText))
	else :
		notFinished = False;
		print("Bye!")
