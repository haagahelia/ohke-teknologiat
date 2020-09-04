import urllib.request
import json

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def hae_postinumerot():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())


def main():
    haettava = input('Kirjoita postinumero: ').strip()

    postinumerot = hae_postinumerot()

    if haettava in postinumerot:
        print(postinumerot[haettava].title())
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
