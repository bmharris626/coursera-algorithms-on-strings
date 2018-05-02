# python3
import sys

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    tree, new = {0: dict()}, 1
    # GOAL: {parent: {'first_letter': [start, length, bool, [child]]}}
    for i in range(len(text)):
        children, letter = [0], text[i]
        while len(children) > 0:
            parent = children.pop()
            # print(tree, parent)

            for c in tree[parent]:
                if len(tree[parent][c]) > 3: children.append(tree[parent][c][-1])
                if c == letter:
                    start, length = tree[parent][c][:2]

                    tree[parent][c][1] -= 1
                    tree[parent][c][2] = False
                    tree[parent][c].append(new)

                    tree[new] = {text[start+length-1]: [start+length-1, 2, True]}
                    # children.append(new)
                    new += 1
                    # print(start, length)

                if tree[parent][c][2]: tree[parent][c][1] += 1
            if tree[parent].get(letter, None) == None:
                tree[parent][letter] = [i, 1, True]
    print(tree)
    return []

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
