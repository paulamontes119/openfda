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
        self.wfile.write(bytes(<html><head><h1>Search OpenFDA Application</h1><h2>Active Ingredient: Here you have the information for the %s drugs</h2><body style="background-color: #87CEFA" >\n<ol>' % (active_ingredient, limit), "utf8"))
        for n in range(len(repos['results'])):
            try:
                for a in range(len(repos['results']["openfda"]))