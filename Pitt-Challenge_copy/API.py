import requests
import json
url = "https://api.fda.gov/drug/label.json"
response = requests.get(url)

query_params = {"gender": "female", "nat": "de"}
endpoint = "https://api.fda.gov/drug/label.json"
requests.get(endpoint, params=query_params).json()

# print(response.status_code)
# print(response.json())



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())