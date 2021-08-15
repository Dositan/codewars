
def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]


assert anagrams("racer", ["crazer", "carer", "racar", "caers", "racer"]) == ["carer", "racer"]
