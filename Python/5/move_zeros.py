
def move_zeros(array):
    new, zeros = [], []
    for x in array:
        zeros.append(x) if x == 0 else new.append(x)
    return new + zeros


assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
