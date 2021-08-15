from math import sqrt


def comp(a, b):
    return sorted(a) == [sqrt(x) for x in sorted(b)]


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
assert comp(a1, a2) is True
