# Reduction algorithm on pages 1082-1083

for x1 in (False, True):
    for x2 in (False, True):
        for x3 in (False, True):
            for x4 in (False, True):
                y3 = True
                if x1==True and x2==False:
                    y3 = False
                y6 = (not x1 and x3) or (x1 and not x3)
                y5 = y6 or x4
                y4 = not y5
                y2 = y3 or y4
                y1 = y2 and (not x2)
                print (int(x1), int(x2), int(x3), int(x4), int(y3), int(y6), int(y5), int(y4), int(y2), int(y1))
