def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    fin_set = set(finnish_words)
    eng_set = set(english_words)

    result = fin_set & eng_set

    print(len(result))


if __name__ == '__main__':
    main()
