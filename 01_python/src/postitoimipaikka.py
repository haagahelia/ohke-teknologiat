import http_pyynto

postinumerot = http_pyynto.hae_postinumerot()

numero = input('Kirjoita postinumero: ')

if numero in postinumerot:
    print(postinumerot[numero])
else:
    print('Tuntematon')
