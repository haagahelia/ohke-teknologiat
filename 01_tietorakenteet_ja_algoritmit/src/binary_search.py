# tiedosto binary_search.py
# tutustu myös valmiiseen toteutukseen https://docs.python.org/3/library/bisect.html
def binary_search(word, list_of_words):
    left = 0
    right = len(list_of_words) - 1

    while left <= right:
        middle = int((left + right) / 2)
        if list_of_words[middle] < word:
            left = middle + 1
        elif list_of_words[middle] > word:
            right = middle - 1
        else:
            return True

    return False
