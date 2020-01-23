import math

m = 20
P = [0 for x in range (m)]
P[1] = 1
for n in range (2,m):
    s = 0
    for k in range (1, n):
        s += P[k] * P[n-k]
    P[n] = s
    a = P[n]
    b = pow(4,n)/pow(n,1.5)
    c = a/b
    d = pow(2,n)
#    print (a, math.floor(b), round(c,3))
    print (n, a, d, round(c,3))
