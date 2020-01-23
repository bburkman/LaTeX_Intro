import math

for t in range (2,100):
    for n in range (2,1000):
        for h in range (2,100):
            if (n+1)/2 == math.pow(t,h):
#                print (t, n, h)
                for g in range (2,h-1):
                    if n+1 == pow(2*t,g+1):
                        print (t, n, h, g)
