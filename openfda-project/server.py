import http.client
import http.server
import json
import socketserver
socketserver.TCPServer.allow_reuse_address = True

PORT = 8005
IP = "localhost"

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        #def documents_sent (document_name):   # We define this function so as to avoid repeating the same process of converting the informatic characters (bytes) into alphabetic ones.
        #    with open(document_name) as f:
        #       message = f.read()

                # WRITE CONTENT AS UTF-8 DATA
        #    self.wfile.write(bytes(message, "utf8"))

        #path = self.path
        if self.path == "/" :
            print("SEARCH: The client is searching a web")
            with open("search.html", 'r') as f:
                message = f.read()
                self.wfile.write(bytes(message, "utf8"))

        elif 'search' in self.path: # let´s try to find a drug and a limit entered by user
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')    #We remove '/search?' and separate the rest at '&'
            drug = info[0].split('=')[1]
            limit = info[1].split('=')[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?search=active_ingredient:"+ drug + '&' + 'limit=' + limit
            print (url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")

            conn.close()
            repos = json.loads(repos_raw)
            self.wfile.write(bytes(json.dumps(repos), "utf8"))
        return

#Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("Server stopped!")