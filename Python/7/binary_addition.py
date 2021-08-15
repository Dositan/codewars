
def add_binary(a, b):
    return format(a + b, "b")


if __name__ == "__main__":
    assert add_binary(1, 1) == "10"
    assert add_binary(5, 3) == "1000"
