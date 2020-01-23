def Print_Optimal_Parens (s, i, j):
    if i==j:
        print ("A_", end='')
        print (i, end=' ')
    else:
        print ("( ", end='')
        Print_Optimal_Parens( s, i, s[i][j] )
        Print_Optimal_Parens( s, s[i][j]+1, j )
        print(") ", end='')


p = [30,35,15,5,10,20,25]
n = len(p) - 1

m = [[0 for x in range (n+1)] for y in range (n+1)]
s = [[0 for x in range (n+1)] for y in range (n)]

for i in range (1, n+1): 
    m[i][i] = 0 # Redundant, but who cares?
for l in range (2, n+1):
    for i in range (1, n-l+2):
        j = i+l-1
        m[i][j] = float ("inf")
        for k in range (i, j):
            q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k

for i in range (1,n+1):
    for j in range (1,n+1):
        if m[i][j]>0:
            print ("%5d " % (m[i][j]), end='')
        else:
            print ("      ", end="")
    print ()
print ()

for i in range (1,n):
    for j in range (2,n+1):
        if s[i][j]>0:
            print ("%2d " % (s[i][j]), end='')
        else:
            print ("   ", end="")
    print ()
print ()

Print_Optimal_Parens(s, 1, 6)
print ()
