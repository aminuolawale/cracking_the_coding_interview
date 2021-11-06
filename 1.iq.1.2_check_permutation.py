"""
Question:
Given two strings, write a method to decide if one is a permutation of the
other.
"""

"""
The most straightforward way is to count the number of each character and compare them for both strings. This will
take up extra space as we would use a hashtable to store the counts but we will have linear time complexity.
"""


def check_permutation(s1: str, s2: str)-> bool:
    s1_char_freqs = get_char_freqs(s1)
    s2_char_freqs = get_char_freqs(s2)
    return s1_char_freqs == s2_char_freqs


def get_char_freqs(s:str)-> dict[str, int]:
    result = dict()
    for char in s:
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result


if __name__ == "__main__":
    s1 = "bead"
    s2 = "deab"
    print(check_permutation(s1, s2))