from wordfiles import get_english_words, get_finnish_words
from binary_search import binary_search


def main():

    english = get_english_words()
    finnish = get_finnish_words()

    for word in finnish:  # tehdään 94 110 kertaa
        if binary_search(word, english):  # tehdään noin 17 kertaa!
            print(word)


if __name__ == "__main__":
    main()
