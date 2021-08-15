
def pig_it(text):
    return " ".join([f"{x[1:]}{x[0]}ay" if x.isalpha() else x for x in text.split()])


assert pig_it("O tempora o mores !") == "Oay emporatay oay oresmay !"
