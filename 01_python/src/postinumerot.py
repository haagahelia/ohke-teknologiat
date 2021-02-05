import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


postinumerot = http_pyynto.hae_postinumerot()

toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()

if toimipaikka in toimipaikat:
    toimipaikat[toimipaikka].sort()

    loydetyt_str = ', '.join(toimipaikat[toimipaikka])
    print('Postinumerot: ' + loydetyt_str)
else:
    print('Toimipaikkaa ei löytynyt')
