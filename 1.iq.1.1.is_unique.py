"""
Question:
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
The easiest method would be to put all the characters in a set and check that the size of the set equals
the size of the string.
"""

def is_unique_0(s: str)-> bool:
    char_set = set(list(s))
    return len(char_set) == len(s)

"""
In the above solution however, we are using an additional data structure. What if we were not allowed to do that?
A brute force way would be to compare each pair of characters.This leads us to an O(N^2) solution.
"""

def is_unique_1(s:str) -> bool:
    for i, char in enumerate(s):
        j = i+ 1
        while j < len(s):
            other_char = s[j]
            if char == other_char:
                return False
            j += 1
    return True

"""
Can we do better than the above solution?
Yes we can. We can sort the string. If we do so, duplicates will be beside eachother. This brings down our complexity to O(NLogN)
"""

def is_unique_2(s:str)-> bool:
    char_list = list(s)
    sorted_char_list = sorted(char_list)
    for index, char in enumerate(sorted_char_list):
        if index > 0 and char == sorted_char_list[index-1]:
            return False
    return True


if __name__ == "__main__":
    s = "ad"
    print(is_unique_0(s))
    print(is_unique_1(s))
    print(is_unique_2(s))


