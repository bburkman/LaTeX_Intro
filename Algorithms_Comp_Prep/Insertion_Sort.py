def Insertion_Sort(A):
    for j in range (1, len(A)):
        key = A[j]
        i = j-1
        print (A[:j], key)
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            print ("   ", A[:j+1])
            i = i-1
        A[i+1] = key
        print ("   ", A[:j+1])
    return A

A = [8,7,6,5,4,3,2,1]
Insertion_Sort(A)
