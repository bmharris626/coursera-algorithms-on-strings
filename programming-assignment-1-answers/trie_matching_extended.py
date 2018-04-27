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
                trie[parent][c] = [False, child]
                child += 1
            if i == len(p) - 1: trie[parent][c][0] = True
            parent = trie[parent][c][1]
    return trie

def prefix_trie_matching(text, trie):
    i, v = 0, 0
    s = text[i]
    while True:
        if trie.get(v, None) == None: return True
        elif trie[v].get(s, None) != None:
            if trie[v][s][0]: return True
            i += 1
            if i >= len(text): return None
            v, s = trie[v][s][1], text[i]
        else: return None

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        match = prefix_trie_matching(text[i:], trie)
        if match: result.append(i)
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
