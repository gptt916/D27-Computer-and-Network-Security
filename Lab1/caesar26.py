''' encrypts the plaintext with a key
    based on the caesar cipher algorithm
    and return the ciphertext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: plaintext matches [a-z]*
'''
def encrypt(key, plaintext):
	ciphertext = ""
	for i in plaintext:
		ciphertext += chr(ord(i)+int(key)%26)
	return ciphertext

''' decrypts the ciphertext with a key
    based on the caesar cipher algorithm
    and returns the plaintext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: ciphertext matches [a-z]*'''    
def decrypt(key, ciphertext):
	plaintext = ""
	for i in ciphertext:
		plaintext += chr(ord(i)-int(key)%26)
	return plaintext
