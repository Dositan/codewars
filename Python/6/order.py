
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda x: sorted(x)))


if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))
