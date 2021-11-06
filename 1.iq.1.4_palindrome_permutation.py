"""
Question:
Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""


def palindrome_permutation(s:str) -> bool:
    """ """
    s = s.lower()
    char_freqs = get_char_freqs(s)
    odd_count = 0
    for k, v in char_freqs.items():
        if v % 2 != 0:
            odd_count += 1
    return odd_count <= 1




def get_char_freqs(s:str)-> dict[str, int]:
    result = dict()
    for char in s:
        if not char.isalpha():
            continue
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result


if __name__ == "__main__":
    s = "Was it a Cat I saw"
    ans = palindrome_permutation(s)
    print(ans)