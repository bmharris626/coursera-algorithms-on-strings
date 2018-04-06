# python3
import sys

class Node:
	def __init__ (self, c):
		self.next = {'A': -1, 'C': -1, 'G': -1, 'T':-1}
		self.length = 0

def build_trie(patterns):
    tree = dict()
    child = 1
    for p in patterns:
        parent = 0
        for i in range(len(p)):
            c = p[i]
            if tree.get(parent, None) == None: tree[parent] = node
            if tree[parent].next[c] == -1:
                tree[parent].next[c] = child
                child += 1
			if i == len(p) - 1:
				node.end = len(p)
				node.word = p
            parent = tree[parent].next[c]
    return tree

def solve (text, n, patterns):
	result = []
	trie = build_trie(patterns)
	for i, c in enumerate(text):
		pass
	# write your code here
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
