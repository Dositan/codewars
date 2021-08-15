
def snail(arr):
    return list(arr[0]) + snail(list(zip(*arr[1:]))[::-1]) if arr else []


if __name__ == "__main__":
    array = snail([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert array == expected
