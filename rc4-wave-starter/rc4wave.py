from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import wave

def encrypt(key_filename, input_filename, output_filename):
    ''' 
    Encrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file.
    (string, string, string) -> None
    '''

    #open input file and retrieve content and header parameter
    wavFile = wave.open(input_filename, 'rb')
    wavBytes = wavFile.readframes(wavFile.getnframes())
    params = wavFile.getparams()
    wavFile.close()

    #open key file and read key into bytes
    keyFile = open(key_filename, 'r')
    keyStr= keyFile.read()
    key = bytes(keyStr, "UTF-8")
    keyFile.close()

    # nonce = Random.new().read(16)
    # tempkey = SHA.new(key+nonce).digest()
    # cipher = ARC4.new(tempkey)

    cipher = ARC4.new(key)

    # msg = nonce + cipher.encrypt(wavBytes)

    msg = cipher.encrypt(wavBytes)

    #open output file, set header parameters and write contents
    wavOut = wave.open(output_filename, 'wb')
    wavOut.setparams(params)
    wavOut.writeframes(msg)
    wavOut.close()

    
def decrypt(key_filename, input_filename, output_filename):
    ''' 
    Decrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file. 
    (string, string, string) -> None
    '''
    #open input file and retrieve content and header parameter
    wavFile = wave.open(input_filename, 'rb')
    wavBytes = wavFile.readframes(wavFile.getnframes())
    params = wavFile.getparams()
    wavFile.close()

    #open key file and read key into bytes
    keyFile = open(key_filename, 'r')
    keyStr= keyFile.read()
    key = bytes(keyStr, "UTF-8")
    keyFile.close()

    #create new cipher with key
    cipher = ARC4.new(key)

    msg = cipher.decrypt(wavBytes)

    #open output file, set header parameters and write contents
    wavOut = wave.open(output_filename, 'wb')
    wavOut.setparams(params)
    wavOut.writeframes(msg)
    wavOut.close()    
