import requests
import pprint

response = requests.get('http://127.0.0.1:8000/regions/regions/')
#
pprint.pprint(response.json())