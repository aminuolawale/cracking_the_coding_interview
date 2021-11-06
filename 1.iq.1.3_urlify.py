"""
Question:
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""

def urlify(word: str, length:int) -> str:
    """ 
    """
    index = 0
    word = list(word)
    while index < len(word):
        if word[index] == " ":
            word[index] = "%20"
        index += 1
    word = word[:length]
    return "".join(word)



if __name__ == "__main__":
    word = "Mr John Smith  "
    print(urlify(word,13))