from wordfiles import get_english_words, get_finnish_words
from binary_search import binary_search


def main():

    english = get_english_words()
    finnish = get_finnish_words()

    # muotoillaan ongelma uudelleen joukko-opin käsitteillä:
    intersection = set(english) & set(finnish)

    for w in intersection:
        print(w)


if __name__ == "__main__":
    main()
