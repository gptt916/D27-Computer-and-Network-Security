import urllib

with open("test.js", "r") as file:
	data=file.read()


print urllib.quote(data)