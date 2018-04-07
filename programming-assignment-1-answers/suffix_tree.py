# python3
import sys

def find_pattern(text, tree, p):
    n = 0

    for key in tree[0]:
        s, l = key[0], key[1]
        if l > len(p):
            for c in text[s:]


            tree[s:len(p)]



        substr = text[key[0]:key[0] + key[1]]


    pass

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    text = "ATAAATG$"
    tree = dict()
    counter = 1
    parent = 0
    for i in range(len(text)):
        if tree.get(parent, None) == None: tree[parent] = {}
        


        parent = 0
        for j in range(len(text) - i):
            c = text[j]
            if tree.get(parent, None) == None: tree[parent] = {}
            if tree[parent].get(c, None) == None:
                tree[parent][c] = counter
                counter += 1
            parent = tree[parent][c]
    print(tree)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))