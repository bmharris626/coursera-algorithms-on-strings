# python3
import sys

def build_trie(text):
    trie = {0: dict()}
    # GOAL: {parent: {'symbol': [position, length, edge]}
    node = 1
    for i in range(len(text)):
        currentNode = 0
        currentSymbol = text[i]
        while True:
            if trie[currentNode].get(currentSymbol, None) == None:
                trie[currentNode][currentSymbol] = [i, len(text)-i, -1]
                break
            elif trie[currentNode][currentSymbol][-1] == -1:
                # Find point of divergence
                position, length, edge = trie[currentNode][currentSymbol]
                print(currentNode, currentSymbol, i, position, length)
                for j in range(length):
                    if text[i+j] == text[position+j]: continue
                    else: break
                # Split currentNode
                trie[node] = {
                    text[i+j]: [i+j, len(text)-i-j, -1],
                    text[position+j]: [position+j, len(text)-position-j, -1]
                }
                print(trie[node])
                # Edit currentNode
                trie[currentNode][currentSymbol][1:3] = [j, node]
                # House Keeping
                node += 1
                break
            else:
                currentNode = trie[currentNode][currentSymbol][-1]
    return trie

def naive_build_trie(text):
    trie = {0: dict()}
    # GOAL: {parent: {'symbol': [position, length, edge]}
    node = 1
    for i in range(len(text)):
        currentNode = 0
        for j in range(i, len(text)):
            currentSymbol = text[j]
            if trie[currentNode].get(currentSymbol, None) == None:
                trie[node] = dict()
                trie[currentNode][currentSymbol] = [j, 1, node]
                currentNode = node
                node += 1
            else:
                currentNode = trie[currentNode][currentSymbol][-1]
        if len(trie[currentNode]) == 0: trie[currentNode][text[i]] = [i, 1, -1]
    return trie

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    # tree = naive_build_trie(text)
    # deletes = list()
    # for node in tree:
    #     for symbol in tree[node]:
    #         if tree[node][symbol][-1] == -1: continue
    #         if len(tree[tree[node][symbol][-1]]) <= 1:
    #             deletes.append(tree[node][symbol][-1])
    #             label = list(tree[tree[node][symbol][-1]].keys())[0]
    #             tree[node][symbol][1] += 1
    #             tree[node][symbol][-1] = tree[tree[node][symbol][-1]][label][-1]
    # for i in deletes: del(tree[i])
    tree = build_trie(text)
    for key in tree:
        print(key, tree[key])
    return []

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
