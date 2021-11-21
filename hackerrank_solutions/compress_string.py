from itertools import groupby

S = [int(n) for n in input()]
occur = [(len(list(group)),key) for key, group in groupby([n for n in S])]
for f in occur:
    print(f,end=' ')