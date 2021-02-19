def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')
    finnish_words.sort()
    english_words.sort()

    fin_index = 0
    eng_index = 0

    while fin_index < len(finnish_words) and eng_index < len(english_words):
        if finnish_words[fin_index] == english_words[eng_index]:
            print(finnish_words[fin_index])
            fin_index += 1
            eng_index += 1
        elif finnish_words[fin_index] < english_words[eng_index]:
            fin_index += 1
        else:
            eng_index += 1


if __name__ == '__main__':
    main()
