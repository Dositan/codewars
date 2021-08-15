
def narcissistic(value):
    val = str(value)
    return sum(int(x) ** len(val) for x in val) == value


assert narcissistic(8208) is True  # 8^4 + 2^4 + 8^4 -> means True
