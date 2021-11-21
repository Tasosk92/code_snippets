#Solution 1
x,k = list(map(int,input().split()))
var = input()
print(eval(var)==k)

#Solution 2
def eval_polynomial(poly, val):
    xs = [ x.strip().replace('^','**') for x in poly.split('+') ]
    return sum( [eval(n.replace('x', str(val))) for n in xs] )

x,k = list(map(int,input().split()))

print(eval_polynomial(input(),x)==k)
