from math import sqrt


def comp(a, b):
    return sorted(a) == [sqrt(x) for x in sorted(b)]


if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) is True
