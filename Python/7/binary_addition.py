
def add_binary(a, b):
    return format(a + b, "b")


assert add_binary(1, 1) == "10"
assert add_binary(5, 3) == "1000"
