from pathlib import Path
import time

# n=94 110
finnish = Path(
    'kotus-sanalista-v1/kotus-sanalista-suomi.txt').read_text().splitlines()

# n=102 401
english = Path('/usr/share/dict/words').read_text().splitlines()


def find_common(fi: list, en: list):
    common = set()
    en_set = set(en)

    for word in fi:  # 94 110
        if word in en_set:  # 1 operaatio!
            common.add(word)

    return common


for size in range(20_000, 130_000, 20_000):
    start = time.perf_counter()
    for i in range(100):
        find_common(finnish[:size], english[:size])
    end = time.perf_counter()
    print(f'{size}  {(end-start)/100}')
