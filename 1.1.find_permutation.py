from collections import defaultdict

def find_permutation(a:str, b:str):
    chars = char_map(a)
    current_map = None
    front = 0
    rear = len(a) -1 
    print(chars, current_map)
    while rear < len(b):
        if current_map is None:
            current_map = char_map(b[:len(a)])
        else:
            current_map[b[front-1]] -= 1
            if current_map[b[front-1]] == 0:
                current_map.pop(b[front-1])
            current_map.update({b[rear]: current_map.get(b[rear], 0)+1})
        if chars == current_map:
            print(front, b[front:rear+1])
        rear += 1
        front += 1
    



def char_map(s:str) -> dict[str,int]:
    result = {}
    for l in s:
        result.update({l:result.get(l,0) +1})
    return result

if __name__ == "__main__":
    find_permutation("aaa", "akavdnkaddaaandkndkeitdnandeititeeitndnfiteandfdakite")