import re
from collections import Counter


def top_3_words(text: str):
    ctr = Counter(re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower()))
    return [x for x, _ in ctr.most_common(3)]


assert top_3_words("   '''   ") == []
assert top_3_words("the dosek dosek dosek is is boy boy") == ["dosek", "is", "boy"]
