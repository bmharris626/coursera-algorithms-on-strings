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

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding
  substrings of the text) in any order.
  """
  result = []
  tree = dict()
  child = 1
  # GOAL: {parent: {(start, end): [bool, child]}}
  for i in range(len(text)):
      parent = 0
      # p = text[:i+1]
      if tree.get(parent, None) == None: tree[parent] = dict()
      for node in tree[parent]:
          # something to determine how many characters are equal
          j, c = node[0], 0
          while (j < node[1]):
              if (text[node[0]:j+1] == text[:i+1][:j+1]): c, j = c+1, j+1
          # if similar then split
          if c > 0:
              # replace old node
              tree[parent][(node[0], node[0]+c-1)] = [False, child]
              # create new node for remainder
              tree[child][(node[0]+c-1, node[1])] = [tree[parent][node][0], tree[parent][node][1]]
              del tree[parent][node]
              # create new node
              tree[child][(0, c)] = [False, ]




  return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
