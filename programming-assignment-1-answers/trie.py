#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
