import json

# JSON-data on tässä kovakoodattu moniriviseksi merkkijonoksi.
# Käytä `open`-funktiota lukeaksesi tiedot levyltä tai
# `urllib`-kirjastoa lukeaksesi tiedot suoraan netistä.
json_merkkijono = """{
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}"""

# json.loads lukee JSON-merkkijonon ja muodostaa Python-rakenteita:
postinumerot_dict = json.loads(json_merkkijono)

# Hakee sanakirjasta postinumeroa vastaavan arvon:
print(postinumerot_dict['73460'])
