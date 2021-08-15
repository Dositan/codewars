
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda x: sorted(x)))


assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
