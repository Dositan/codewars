def narcissistic(value):
    val = str(value)
    return sum(int(x) ** len(val) for x in val) == value


if __name__ == "__main__":
    print(narcissistic(8208))  # 8^4 + 2^4 + 8^4
