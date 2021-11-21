from itertools import combinations

comb = []
s,num = list(input().split())
for i in range(1,int(num)+1):
    comb.append(list(combinations(s,i)))
comb = [''.join((sorted(item))) for sublist in comb for item in sublist]
comb.sort(key=lambda item: (len(item), item))
for c in comb:
    print(c)
