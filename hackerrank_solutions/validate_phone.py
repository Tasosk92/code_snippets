import re

n = int(input())
for _ in range(n):
    s = input()
    if ((len(s))==10 and s.isdigit()) and re.match(r'^[7-9]', s):
        print("YES")
    else:
        print("NO")