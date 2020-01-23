import math


#n = 5
#p = [0.00, 0.10, 0.11, 0.12, 0.13, 0.15]
#q = [0.04, 0.05, 0.06, 0.07, 0.08, 0.09]

n = 7
p = [1/n for i in range (n+1)]
p[0] = 0
q = [0 for i in range (n+1)]

print (sum(p) + sum(q))

e = [[0.0 for y in range (n+1)] for x in range (n+2)]
w = [[0.0 for y in range (n+1)] for x in range (n+2)]
root = [[0.0 for y in range (n+1)] for x in range (n+1)]

for i in range (1,n+2):
    e[i][i-1] = q[i-1]
    w[i][i-1] = q[i-1]

for l in range (1,n+1):
    for i in range (1, n-l+2):
        j = i+l-1
        e[i][j] = 100.0
        w[i][j] = w[i][j-1] + p[j] + q[j]
        for r in range (i, j+1):
            t = e[i][r-1] + e[r+1][j] + w[i][j]
            if t < e[i][j]:
                e[i][j] = t
                root[i][j] = r
        print (l, i, j)
        for a in range (1,n+2):
            for b in range (0, n+1):
                print ("%3.2f  " % (e[a][b]), end='')
            print ("\\cr")
        print ()
        for a in range (1,n+2):
            for b in range (0, n+1):
                print ("%3.2f " % (w[a][b]), end='')
            print ("\\cr")
        print ()
        for a in range (1,n+1):
            for b in range (1, n+1):
                print ("%d  " % (root[a][b]), end='')
            print ("\\cr")
        print ()


for i in range (1,n+2):
    print (i, end='')
    for j in range (0,n+1):
        print (" & ", end='')
        if e[i][j]>0:
            print ("%3.2f " % (e[i][j]), end='')
    print (" \\cr")
print ()

for i in range (1,n+2):
    print (i, end='')
    for j in range (0,n+1):
        print (" & ", end='')
        if w[i][j]>0:
            print ("%3.2f " % (w[i][j]), end='')
    print (" \\cr")
print ()

for i in range (1,n+1):
    print (i, end='')
    for j in range (1,n+1):
        print (" & ", end='')
        if root[i][j]>0:
            print ("%d " % (root[i][j]), end='')
    print (" \\cr")
print ()


