
def descending_order(num):
    desc = sorted(str(num), reverse=True)
    return int(''.join(desc))


assert descending_order(19283) == 98321
