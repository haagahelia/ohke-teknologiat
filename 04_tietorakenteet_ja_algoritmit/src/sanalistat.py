def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    for word in finnish_words:  # n = 94 110
        if word in english_words:  # m = 102 401
            print(word)


if __name__ == '__main__':
    main()
