def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def binary_search(all_words, search_word):
    if len(all_words) == 0:
        return False

    middle = len(all_words) // 2
    if all_words[middle] < search_word:
        bigger = all_words[middle + 1:]
        return binary_search(bigger, search_word)
    elif all_words[middle] > search_word:
        smaller = all_words[0:middle]
        return binary_search(smaller, search_word)
    else:
        return True


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')
    finnish_words.sort()
    english_words.sort()

    for word in finnish_words:  # reilut 90 000
        if binary_search(english_words, word):  # noin 16
            print(word)


if __name__ == '__main__':
    main()
