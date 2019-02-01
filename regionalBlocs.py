import requests
import json
r = requests.get("https://restcountries.eu/rest/v2/region/europe")
for item in r.json():
 t = item['regionalBlocs']
 for a in t:
  print(a['name'])