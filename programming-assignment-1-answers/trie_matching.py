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

def prefix_trie_matching(text, trie):
    i, v = 0, 0
    s = text[i]
    while True:
        if trie.get(v, None) == None: return text[:v]
        elif trie[v].get(s, None) != None:
            i += 1
            v = trie[v][s]
            if i < len(text): s = text[i]
            elif i > len(text): return None
        else: return None

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    print(trie)
    for i in range(len(text)):
        pattern = prefix_trie_matching(text[i:], trie)
        if pattern != None: result.append(i)
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
