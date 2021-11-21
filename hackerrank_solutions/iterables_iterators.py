import itertools

N = int(input())
letters = input().split()
K = int(input())

C = list(itertools.combinations(letters,K))
F = list(filter(lambda c: 'a' in c, C))

print(len(F)/len(C))