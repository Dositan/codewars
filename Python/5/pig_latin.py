
def pig_it(text):
    return " ".join([f"{x[1:]}{x[0]}ay" if x.isalnum() else x for x in text.split()])


if __name__ == "__main__":
    print(pig_it("O tempora o mores !"))
