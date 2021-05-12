import requests
import json

parameters = {
    "ids": "BTC,ETH,XRP",
    "interval": "1d",
    "convert": "USD",
    "status": "active"
}

response = requests.get("https://api.nomics.com/v1/currencies/ticker?key=cd97e04b2349eca6ffd4780ab849b1061325bd63&&,30d&&per-page=100&page=1")
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())