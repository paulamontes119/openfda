import http.server
import socketserver
import http.client
import json

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8001

# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):

        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()


def search_drug(active_ingredient, limit):  # called to search for a drug and a limit

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    print("The client has succesfully made a request!")
    conn.request("GET", "/drug/label.json?search=active_ingredient:%s&limit=%s" % (active, limit), None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)

    with open ("data_drugs.html", "w"):
        self.wfile.write(bytes('<html><head><h1>Search OpenFDA Application</h1><h2>Active Ingredient: "Here you have the information of the" %s "drugs"</h2><body style="background-color: #87CEFA" ></body> </html>' % (active_ingredient, limit), "utf8"))
        for n in range(len(repos['results'])):
            try:
                for a in range(len(repos['results']["openfda"]["brand_name"])):
                    try:
                        drug = "<li>" + "The brand name of the drug that has been chosen: " + repos['results'][i]["openfda"]["brand_name"][0] + "</li>"
                        self.wfile.write(bytes(drug, "utf8"))
                    except KeyError:
                        break

            except KeyError:
                drug = "<li>" + "The brand name of this drug is not found" + "</li>"
                self.wfile.write(bytes(drug, "utf8"))
                continue

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


