
def move_zeros(array):
    new, zeros = [], []
    for x in array:
        zeros.append(x) if x == 0 else new.append(x)
    return new + zeros


if __name__ == "__main__":
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
