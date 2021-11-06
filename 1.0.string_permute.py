#Algorithm:
# for each character in the string, permute the other characters. Keep a prefix which is recursively grown by the current character.
# Eventually, the current string will become empty and the prefix would have grown to the length of the original string, now we can print the prefix as a permutation.

def permute(s:str, pref: str= "") :
    if len(s) == 0:
        print(pref)
    for i, l in enumerate(s):
        rem = s[:i] + s[i+1:]
        permute(rem, pref + l)
    

if __name__  == "__main__":
    permute("abc")