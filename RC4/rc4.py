def rc4(key, inputStream):
	''' returns the RC4 encoding of inputStream based on the key
	(bytes, bytes) -> bytes
	'''
	S=KSA(key)
	keystream = PRGA(S)
	rettext=bytearray()
	for c in inputStream:
		xor_byte = c^next(keystream)
		rettext.append(xor_byte)
	return rettext

def KSA(key):
	keylen = len(key)

	S = list(range(0,256))
	j = 0
	for i in range(0, 256):
		j = (j + S[i] + key[i%keylen])%256
		S[i], S[j] = S[j], S[i]
	return S

def PRGA(S):
	i = 0
	j = 0
	while True:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i] 

		K = S[(S[i] + S[j]) % 256]
		yield K