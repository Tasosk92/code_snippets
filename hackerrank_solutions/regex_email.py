import re
regex = r'\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{0,3}\b'
def fun(s):
    if(re.fullmatch(regex, s)):
        return True
 
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
