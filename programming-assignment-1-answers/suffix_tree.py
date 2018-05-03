# python3
import sys

def build_trie(patterns):
    trie = dict()
    child = 1
    for p in patterns:
        parent = 0
        for i in range(len(p)):
            c = p[i]
            if trie.get(parent, None) == None: trie[parent] = {}
            if trie[parent].get(c, None) == None:
                trie[parent][c] = child
                child += 1
            parent = trie[parent][c]
    return trie

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    tree, new = {0: dict()}, 1
    # GOAL: {parent: {'first_letter': [start, length, suffixCount, child]}
    #   Rule1: Adds new character to existing leaf edge
    #   Rule2: Creates new leaf edge
    #   Rule3: Ends current phase
    for i in range(len(text)):
        children, letter = [0], text[i]
        while len(children) > 0:
            parent = children.pop()
            # print(tree, parent)

            for c in tree[parent]:
                if tree[parent][c][-1] == None: tree[parent][c][1] += 1
                if c == letter: tree[parent][c][2] += 1
                if tree[parent][c][2] > 0:
                    if tree[parent][c][-1] == None:
                        tree[new] = dict()
                        tree[parent][c][-1] = new
                        new += 1
                    for j in range(tree[parent][c][2]):
                        k = text[tree[parent][c][0] + j + 1]
                        if k == letter: tree[parent][c][2] += 1
                        else:
                            start, length, suffixCount, child = tree[parent][c]
                            # Create two new nodes from split
                            tree[child][letter] = [i, 1, 0, None]
                            tree[child][k] = [start+j+1, length-(j+1), 0, None]
                            # Edit the old node
                            tree[parent][c][1] = j+1
                            tree[parent][c][2] = j-1

            if tree[parent].get(letter, None) == None:
                tree[parent][letter] = [i, 1, 0, None]
    print(tree)
    return []

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
