# python3
import sys

def InverseBWT(bwt):
    # write your code here
    first_column = "".join(sorted(bwt))
    first_column = first_column[1:] + first_column[0]

    """" Build dictionary
        {'$': [loc, ...]}
    """
    idx = dict()

    for i in range(len(bwt)):
        c_first = first_column[i]
        c_last = bwt[i]

        idx[c] = idx.get(c, list()) + [first_column[i]]

        idx_first[c_first] = idx_first.get(c_first, list()) + [i]
        idx_last[c_last] = idx_first.get(c_last, list()) + [i]

    c = bwt[-1]
    for i in range(len(bwt)):
        idx_last[c]

    return ""

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))