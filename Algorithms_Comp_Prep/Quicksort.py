count = 0

def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range (p, r):
        if A[j]<=x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    print ("  x, A = ", x, A)
    return i+1

def Quicksort(A, p, r):
    print ("\n(p,r) = ",p, r)
    print ("Partition the array ", A[p:r+1])
    print ("Pivot at A[r] =", A[r])
    if p<r:
        q = Partition(A, p, r)
        global count
        count = count + 1
        print ("    dividing the array into subarrays", A[p:q], ",", A[q], ", and", A[q+1:r+1], ".")
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)


#A = [2,8,7,1,3,5,6,4]
#A = [1,2,3,4,5,6,7,8]
A = [1,3,4,5,7,6,4]
print ("A = ", A)
print ()

#Partition(A,0,len(A)-1)
Quicksort(A, 0, len(A)-1)
print ("Number of calls of Quicksort function = ", count)
