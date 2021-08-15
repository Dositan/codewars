# NOTE: NOT DONE YET!

import re


def strip_comments(string: str, prefix: str = "(#|//)") -> str:
    comment = re.compile(f"{prefix}.*")
    lines = [comment.sub("", line) for line in string.split("\n")]
    return "\n".join(lines) 


if __name__ == "__main__":
    print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
