import http.server
import socketserver
import http.client
import json

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000
socketserver.TCPServer.allow_reuse_address = True

# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):

        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()


        def active_ingredient():  # called to search for a drug and a limit

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            drug = info[0].split('=')[1]
            limit = info[1].split('=')[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?search=active_ingredient:" + drug + '&' + 'limit=' + limit
            print(url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")

            conn.close()
            repos = json.loads(repos_raw)



            my_list = []
            a = 0
            start_list = "<head>" +  "THIS ARE THE BRAND NAMES OF THE DRUGS THAT YOU ARE LOOKING FOR: " + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    a += 1
                except KeyError:
                    my_list.append("")
                    a += 1

            with open ("data_drugs.html", "w") as f:
                f.write(start_list)
                for element in my_list:
                    list_elements = "<t>" + "<li>" + element
                    f.write(list_elements)

        if self.path == "/":
            print("SEARCH: The client is searching a web")
            with open("search.html", 'r') as f:
                message = f.read()
                self.wfile.write(bytes(message, "utf8"))
        elif 'active' in self.path:  # let´s try to find a drug and a limit entered by user
            active_ingredient()

            with open("data_drugs.html", "r") as f:
                pauli = f.read()
                self.wfile.write(bytes(pauli,"utf8"))

# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at %s:%s" % (IP, PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print("")
print("Server stopped!")


