# -*- coding: utf-8 -*-
bits = """                              �H��5�Y��ӄ�H�c(X���z�e\�v��,���۾�?���dT���zo�u�i�u�/��B��z���=��y��g֫+���1F&���;��cv����
$��Jh�D�n��\ȳ��X(*56V"""
from hashlib import sha256
if (sha256(bits).hexdigest() == "31dbc4b78a086cf887f39ba100fdf41b602cb0d8d7bffa15e2ad90100db4d8b0"):
	print "I am good!"
else:
	print "I am evil!"
