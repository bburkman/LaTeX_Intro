W = 6
n = 5
w = [0,5,4,3,2,1]
v = [0,1,2,3,4,5]
Memo = [[0 for x in range (W+1)] for y in range (n+1)]
List = [["" for x in range (W+1)] for y in range (n+1)]

for i in range (n+1):
    for j in range (W+1):
        if i==0 or j==0:
            Memo[i][j] = 0
        # If the weight of the object we're considering
        # is less than the knapsack capacity we're considering, 
        # then go with the knapsack value for that capacity 
            # without that object, i.e. 
        # the value in the row above.  
        elif w[i]>j:
            Memo[i][j] = Memo[i-1][j]
        else:
            # Given that the current knapsack capacity is j, 
                # and the object we're considering has weight w[i],
            # We could fit it into a knapsack with j-w[i] pounds.
            # The current value of the optimal mix for j-w[i] pounds
                # is in Memo[i-1][j-w[i]].  
            # If adding object i would give us a better total value at weight j
                # than the current optimal value, Memo[i-1][j], 
            # Then add it.  

            # Also, keep track of which objects are in the bag.  

            Memo[i][j] = Memo[i-1][j]
            List[i][j] = List[i-1][j]
            if Memo[i-1][j-w[i]] + v[i] > Memo[i-1][j]:
                Memo[i][j] = Memo[i-1][j-w[i]] + v[i]
                List[i][j] = List[i-1][j-w[i]] + " " + str(i)
                if List[i][j] != List[i][j-1]:
                    print ("List is now ", List[i][j])

for row in Memo:
    print (row)

for row in List:
    print (row)
            
print ()
print ("Max value is ", Memo[n][W], "with objects ", List[n][W])
