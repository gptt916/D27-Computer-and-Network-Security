import httplib, urllib
params = urllib.urlencode({'username': 'alice', 'password': 'pass4alice', 'action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = httplib.HTTPConnection("http-only.seclab.space")
conn.request("POST", "", params, headers)
response = conn.getresponse()

print response.status, response.reason

data = response.read()

print data

conn.close()