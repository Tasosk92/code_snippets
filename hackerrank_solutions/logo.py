import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict

if __name__ == '__main__':
    s = 'qwertyuiopasdfghjklzxcvbnm'
    #s = 'bbaaccbed'
    s = 'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni'
    for key,value in Counter(sorted(s)).most_common()[:3]:
        print(key,value)

#if __name__ == '__main__':
#    s = input()
#    c = Counter(s)
#    a = sorted(c.items(), key=lambda item: (-item[1], item[0]))[:3]
#    for tup in a:
#        print(tup[0],tup[1])
