
def array_diff(a, b):
    return [x for x in a if x not in b]


assert array_diff([1,2],[1]) == [2]
