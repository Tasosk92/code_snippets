from collections import Counter

num = int(input())
words = Counter()
for _ in range(num):
    word = input()
    words.update({word:1})
print(len(words.keys()))
for value in words.values():
    print(value,end=' ')


from collections import OrderedDict

num = int(input())
words = OrderedDict()
for _ in range(num):
    word = input()
    if word in words.keys():
        words[word] +=1
    else:
        words[word] =1

print(len(words.keys()))
for value in words.values():
    print(value,end=' ')
