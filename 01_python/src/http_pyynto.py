import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
    data = response.read()

postinumerot = json.loads(data)

print(postinumerot['00100'])
