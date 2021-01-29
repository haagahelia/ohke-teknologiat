import json

with open('postinumerot.json') as f:
    tiedoston_sisalto = f.read()

print(len(tiedoston_sisalto))

postinumerot = json.loads(tiedoston_sisalto)

print(postinumerot['00100'])
