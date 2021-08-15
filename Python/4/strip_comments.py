# NOTE: NOT DONE YET!
import re


def strip_comments(string, prefix = "(#|//)"):
    comment = re.compile(f"{prefix}.*")
    lines = [comment.sub("", line) for line in string.split("\n")]
    return "\n".join(lines) 


assert strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples\ngrapes\nbananas"
