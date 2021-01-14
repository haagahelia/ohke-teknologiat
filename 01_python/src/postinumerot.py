from postitoimipaikka import hae_postinumerot


def main():
    postinumerot = hae_postinumerot()

    toimipaikat_ja_numerot = {}

    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]

    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()

    if etsittava in toimipaikat_ja_numerot:
        loydetyt = toimipaikat_ja_numerot[etsittava]
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
