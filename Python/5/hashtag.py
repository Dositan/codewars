
def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    return "#" + "".join(x.capitalize() for x in s.split())


if __name__ == "__main__":
    print(generate_hashtag("   Hello    World    "))
