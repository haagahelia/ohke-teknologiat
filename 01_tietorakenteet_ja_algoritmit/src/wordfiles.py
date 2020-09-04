

# funktio, joka lukee suomenkieliset sanat:
def get_finnish_words():
    with open('kotus-sanalista-v1/kotus-sanalista-suomi.txt', encoding='utf-8') as file:
        return file.read().lower().splitlines()


def get_english_words():
    with open('/usr/share/dict/words', encoding='utf-8') as file:
        return file.read().lower().splitlines()
