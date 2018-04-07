# python3
import sys

NA = -1

class Node:
    def __init__(self):
        self.next = {'A': NA, 'C': NA, 'G': NA, 'T': NA}
        self.word = None

def build_trie(patterns):
    tree = [Node()]
    counter = 1
    for p in patterns:
        parent = 0
        for c in p:
            if len(tree) <= counter: tree.append(Node())
            if tree[parent].next[c] == NA: 
                tree[parent].next[c] = counter
                counter += 1
            if tree[parent].next[c] == NA: break
            parent = tree[parent].next[c]
        tree[parent].word = p
    return tree

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i, c in enumerate(text):
        n, j = 0, i
        while n != NA:
            c = text[j]
            n = trie[n].next[c]
            if (n != -1) and (trie[n].word != None): 
                result.append(i)
                break
            j += 1
            if j == len(text): break
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
