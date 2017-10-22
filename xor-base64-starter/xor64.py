from Crypto.Cipher import XOR

''' encrypts the plaintext (utf-8) with a key
    based on the xor cipher algorithm
    and return the ciphertext (base64 encoded)
    (string, string) -> string
'''
def encrypt(key, plaintext):
    encryption = XOR.new(key)
    ciphertext = encryption.encrypt(plaintext)
    return ciphertext.decode("utf-8")

''' decrypts the ciphertext (base64 encoded) with a key
    based on the xor cipher algorithm
    and returns the plaintext (utf-8)
    (string, string) -> string
'''    
def decrypt(key, ciphertext):
    decryption = XOR.new(key)
    plaintext = decryption.encrypt(ciphertext)
    return plaintext.decode("utf-8")