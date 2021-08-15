
def snail(arr):
    return list(arr[0]) + snail(list(zip(*arr[1:]))[::-1]) if arr else []


expected = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
array = snail(expected)
assert array == expected
