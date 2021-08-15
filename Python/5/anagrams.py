from typing import List


def anagrams(word: str, words: List[str]) -> List[str]:
    """Anagrams are the list of words with same letters.

    In this kata we have to return the list of anagrams for the given word.

    Args:
        word (str): Word to find anagrams for.
        words (List[str]): List of words to sort through.

    Returns:
        List[str]: The list of anagram words.
    """
    return [x for x in words if sorted(x) == sorted(word)]


if __name__ == "__main__":
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
