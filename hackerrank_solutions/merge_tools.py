from collections import OrderedDict

def merge_the_tools(string, k):
    sub =  [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(sub)):
        print(''.join(OrderedDict.fromkeys(sub[i])))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)