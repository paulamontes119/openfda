import http.client
import http.server
import json
import socketserver
socketserver.TCPServer.allow_reuse_address = True

PORT = 8000
IP = "localhost"

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        def documents_sent (document_name):   # We define this function so as to avoid repeating the same process of converting the informatic characters (bytes) into alphabetic ones.
            with open(document_name) as f:
                message = f.read()

                # WRITE CONTENT AS UTF-8 DATA
            self.wfile.write(bytes(message, "utf8"))

        if self.path == "/" :
            documents_sent("search.html")

        elif self.path == "/drug":

            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPSConnection("api.fda.gov")
            conn.request("GET", "/drug/label.json?", None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()

            repos = json.loads(repos_raw)


        else:
            with open("error.html.","r") as f:
                error = f.read()
                message = error