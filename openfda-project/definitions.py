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
            start_list = "<head>" + "<h2>" + "THESE ARE THE BRAND NAMES OF THE DRUGS THAT YOU ARE LOOKING FOR:" + '<body style="background-color: #ff99bb">' + "</h2>" + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    a += 1
                except KeyError:
                    my_list.append("Not known")
                    a += 1

            with open ("data_drugs.html", "w") as f:
                f.write(start_list)
                for element in my_list:
                    list_elements = "<t>" + "<li>" + element
                    f.write(list_elements)

        def manufacturer_name():

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            manufacturer_name = info[0].split('=')[1]
            limit = info[1].split('=')[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?search=openfda.manufacturer_name:" + manufacturer_name + '&' + 'limit=' + limit
            print(url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            my_list = []
            a = 0
            start_list = "<head>" + "<h2>" + "THIS ARE THE MANUFACTURE NAMES' OF THE DRUGS THAT YOU ARE LOOKING FOR:" + '<body style="background-color: #ff99bb">' + "</h2>" + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    a += 1
                except KeyError:
                    my_list.append("Not known")
                    a += 1

            with open("manufacturer_name.html", "w") as f:
                f.write(start_list)
                for element in my_list:
                    list_elements = "<t>" + "<li>" + element
                    f.write(list_elements)


        def list_drugs():
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            limit = info[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?limit=" + limit
            print(url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            my_list = []
            a = 0
            start_list = "<head>" + "<h2>" + "THIS IS THE LIST OF ALL DRUGS YOU ARE LOOKING FOR:" + '<body style="background-color: #ff99bb">' + "</h2>" + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    a += 1
                except KeyError:
                    my_list.append("Not known")
                    a += 1

            with open("drugs_list.html", "w") as f:
                f.write(start_list)
                for element in my_list:
                    list_elements = "<t>" + "<li>" + element
                    f.write(list_elements)


        def list_manufacturers():
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            limit = info[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?limit=" + limit
            print(url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            my_list = []
            a = 0
            start_list = "<head>" + "<h2>" + "THIS IS THE LIST OF ALL MANUFACTURERS YOU ARE LOOKING FOR:" + '<body style="background-color: #ff99bb">' + "</h2>" + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    a += 1
                except KeyError:
                    my_list.append("Not known")
                    a += 1

            with open("manufacturers_list.html", "w") as f:
                f.write(start_list)
                for element in my_list:
                    list_elements = "<t>" + "<li>" + element
                    f.write(list_elements)


        def list_warnings():
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            info = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            limit = info[1]
            print("The client has succesfully made a request!")

            url = "/drug/label.json?limit=" + limit
            print(url)

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            my_list = []
            a = 0
            start_list = "<head>" + "<h2>" + "THIS IS THE LIST OF ALL MANUFACTURERS YOU ARE LOOKING FOR:" + '<body style="background-color: #ff99bb">' + "</h2>" + "</head>" "<ol>" + "\n"
            nlimit = int(limit)

            while a < nlimit:
                try:
                    my_list.append(repos['results'][a]["openfda"]['brand_name'][0])
                    my_list.append(repos['results'][a]['warnings'][0])
                    a += 1
                except KeyError:
                    my_list.append("Not known")
                    a += 1

            with open("warnings_list.html", "w") as f:
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

        elif 'Company' in self.path:  # let´s try to find a drug and a limit entered by user
            manufacturer_name()

            with open("data_drugs.html", "r") as f:
                pauli = f.read()
                self.wfile.write(bytes(pauli, "utf8"))

        elif 'listDrugs' in self.path:  # let´s try to find a drug and a limit entered by user
            list_drugs()

            with open("data_drugs.html", "r") as f:
                pauli = f.read()
                self.wfile.write(bytes(pauli, "utf8"))

        elif 'listCompanies' in self.path:  # let´s try to find a drug and a limit entered by user
            list_manufacturers()

            with open("data_drugs.html", "r") as f:
                pauli = f.read()
                self.wfile.write(bytes(pauli, "utf8"))

        elif 'listWarnings' in self.path:  # let´s try to find a drug and a limit entered by user
            list_manufacturers()

            with open("data_drugs.html", "r") as f:
                pauli = f.read()
                self.wfile.write(bytes(pauli, "utf8"))


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


