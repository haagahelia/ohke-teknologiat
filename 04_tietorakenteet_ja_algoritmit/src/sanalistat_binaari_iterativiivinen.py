def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def binary_search(list_of_words, word):
    left = 0
    right = len(list_of_words) - 1

    while left <= right:
        middle = (left + right) // 2
        if list_of_words[middle] < word:
            left = middle + 1
        elif list_of_words[middle] > word:
            right = middle - 1
        else:
            return True

    return False


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
