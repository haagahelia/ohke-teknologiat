from wordfiles import get_english_words, get_finnish_words


def main():

    english = get_english_words()
    finnish = get_finnish_words()

    for word in finnish:  # tehdään 94 110 kertaa
        if word in english:  # tehdään jopa 102 401 kertaa!
            print(word)


if __name__ == "__main__":
    main()
