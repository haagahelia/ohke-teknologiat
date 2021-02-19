def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    english_dict = {}
    for w in english_words:  # 102 401
        english_dict[w] = True

    for word in finnish_words:  # n = 94 110
        if word in english_dict:
            print(word)

    # 1. versio: O(m * n)
    # 2. versio: O(m * log2(n)) logaritminen
    # 3. versio: O(n) lineaarinen


if __name__ == '__main__':
    main()
