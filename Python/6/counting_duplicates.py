from collections import Counter


def duplicate_count(text):
    return sum(1 for x in Counter(text.lower()).values() if x > 1)


assert duplicate_count('aboba') == 2
assert duplicate_count('Indivisibilities') == 2
