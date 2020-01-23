# Boolean expression for phi' on page 1083

def IFF (a, b):
    return (a and b) or (not a and not b)

def IMPLIES (a, b):
    if a==True and b==False:
        return 0
    return 1

for a in (False, True):
    for b in (False, True):
        c = IFF(a,b)
        d = IMPLIES(a,b)
        for z in (a,b,c,d):
            print (int(z), end=' ')
        print ()
print ()

for y1 in (True, False):
    for y2 in (True, False):
        for x2 in (True, False):
            a = y2 and not x2
            b = IFF(y1, a)
            for z in (y1, y2, x2, b):
                print (int(z), end=' ')
            print ()
print ()

for x1 in (True, False):
    for x2 in (True, False):
        for y1 in (True, False):
            a = IMPLIES(x1,x2)
            b = IFF (y1, a)
            c = y1 and b
            for z in (x1, x2, y1, a, b, c):
                print (int(z), end=' ')
            print ()
print ()

for x1 in (False, True):
    for x2 in (False, True):
        for x3 in (False, True):
            for x4 in (False, True):
                for y1 in (False, True):
                    for y2 in (False, True):
                        for y3 in (False, True):
                            for y4 in (False, True):
                                for y5 in (False, True):
                                    for y6 in (False, True):
                                        phi = (
                                            y1 and 
                                            IFF (y1, y2 and not x2) and 
                                            IFF (y2, y3 or y4) and
                                            IFF (y3, IMPLIES(x1, x2)) and
                                            IFF (y4, not y5) and 
                                            IFF (y5, y6 or x4) and
                                            IFF (y6, IFF(not x1, x3))
                                           )
                                        if phi==True:
                                            for z in (x1, x2, x3, x4, y1, y2, y3, y4, y5, y6, phi):
                                                print (int(z), end=' & ')
                                            print (" \\cr")
