from wordfiles import get_english_words, get_finnish_words
from binary_search import binary_search


def main():

    english = get_english_words()
    finnish = get_finnish_words()

    english_dict = {w: True for w in english}  # dict comprehension

    for word in finnish:  # tehdään 94 110 kertaa
        if word in english_dict:  # tehdään noin 1 kerran!
            print(word)


if __name__ == "__main__":
    main()
