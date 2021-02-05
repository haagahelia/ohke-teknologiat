import http_pyynto


def etsi_toimipaikka(postinumero):
    postinumerot = http_pyynto.hae_postinumerot()

    if postinumero in postinumerot:
        return postinumerot[postinumero]
    else:
        return 'Tuntematon'


def main():
    numero = input('Kirjoita postinumero: ')

    print(etsi_toimipaikka(numero))


if __name__ == '__main__':
    main()
