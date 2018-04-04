import http.client
import json

# Send a query using the following url
# https://api.fda.gov/drug/label.json?search=active_ingredient:acetylsalicylic&limit=4
# https://api.fda.gov/drug/event.json?search=field:term

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov") # It changes too
conn.request("GET", "/drug/label.json?search=active_ingredient:acetylsalicylic&limit=4", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()
repos = json.loads(repos_raw)

print("The name of the manufacturer repository is", repos["results"][0]["openfda"]["manufacturer_name"])
print("The name of the manufacturer repository is", repos["results"][2]["openfda"]["manufacturer_name"])