# _*_ coding:UTF-8 _*_
# b64 decode and encode

import base64


def b64encode(string):
    a = base64.b64encode(string.encode())
    return a.decode()

def b64decode(string):
    a = base64.b64decode(string).decode()
    return a

def b32encode(string):
	a = base64.b32encode(string.encode())
	return a.decode()

def b32decode(string):
	a = base64.b32decode(string).decode()
	return a

def b16decode(string):
	a = base64.b16decode(string).decode()
	return a

def b16encode(string):
	a = base64.b16encode(string.encode())
	return a.decode()

def b85encode(string):
	a = base64.b85encode(string.encode())
	return a.decode()

def b85decode(string):
	a = base64.b85decode(string).decode()
	return a

