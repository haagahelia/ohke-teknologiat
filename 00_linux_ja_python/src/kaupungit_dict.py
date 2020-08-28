# dict -rakenteet, eli sanakirjat, vastaavat map-rakenteita:
kaupungit = {
    'Helsinki': 648553,
    'Espoo': 285018,
    'Vantaa': 229593
}

# arvojen (väkiluvut) hakeminen avaimien (nimet) perusteella:
print(kaupungit['Helsinki'])
print(kaupungit['Vantaa'])

# uuden avaimen ja arvon asettaminen:
kaupungit['Kauniainen'] = 9549

# tulostetaan koko rakenne
print(kaupungit)


# in -operaatio hakee sanakirjan _avaimista_
if 'Helsinki' in kaupungit:
    print('Helsinki löytyy kaupungeista')

if 'Tampere' in kaupungit:  # ei löydy
    print(kaupungit['Tampere'])

# Arvoa haetaan vain _avaimista_ eli kaupunkien nimistä
print(9549 in kaupungit)  # false

print(kaupungit.keys())  # tulostaa listan avaimia, eli kaupunkien nimet

print(kaupungit.values())  # tulostaa listan arvoja, eli väkiluvut

# väkilukujen summa saadaan laskettua kätevästi sum-funktiolla!
vakiluku_yhteensa = sum(kaupungit.values())
print(vakiluku_yhteensa)

# kerätään tähän listaan kaupungit, joissa on yli 50000 asukasta!
isot_kaupungit = []

# for a, b in x.items() käy läpi avaimet ja arvot *pareittain*
for kaupunki, vakiluku in kaupungit.items():
    if vakiluku > 50000:
        # lisätään uusi kaupungin nimi listalle
        isot_kaupungit.append(kaupunki)

# tulostaa isojen kaupunkien nimet
print(isot_kaupungit)


kaupungit['Tukholma'] = 975904
print(kaupungit)

# del -komennolla poistetaan sekä avain että siihen liitetty arvo:
del kaupungit['Tukholma']

# Tukholma on nyt poistettu
print(kaupungit)
