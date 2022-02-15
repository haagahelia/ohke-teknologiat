from pathlib import Path
import time

# n=94 110
finnish = Path(
    'kotus-sanalista-v1/kotus-sanalista-suomi.txt').read_text().splitlines()
finnish.sort()

# n=102 401
english = Path('/usr/share/dict/words').read_text().splitlines()
english.sort()


def binary_search(search: str, words: list) -> bool:
    min = 0
    max = len(words) - 1

    while min <= max:
        mid = (max + min) // 2
        if search == words[mid]:
            return True
        elif search < words[mid]:
            max = mid - 1
        elif search > words[mid]:
            min = mid + 1

    return False


def find_common(fi, en):
    common = []

    # n * log2(n)
    for word in fi:  # 94 110
        if binary_search(word, en):  # log2(n)
            common.append(word)

    return common


for size in range(20_000, 110_000, 20_000):
    start = time.perf_counter()
    find_common(finnish[:size], english[:size])
    end = time.perf_counter()
    print(f'{size}  {end-start}')
