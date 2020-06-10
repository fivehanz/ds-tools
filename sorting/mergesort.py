"""
Mergesort        
Converted from C 
"""


def merge(A, low, mid, high):
    """ in-place merge """

    i, j, k = low, mid+1, low
    B = [None] * len(A)
    
    """ Comparing two lists """
    while i <= mid and j <= high:
        if A[i] < A[j]:
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1
        k+=1

    """ add the leftover list items """
    while i <= mid:
        B[k] = A[i]
        k+=1
        i+=1
    
    while j <= high:
        B[k] = A[j]
        k+=1
        j+=1

    """ Copying all items back to A """
    i = 0
    while (i < len(A)):
        if B[i] != None: ### Some pythonic errors
            A[i] = B[i]
        i += 1


def mergesort(A, low, high):
    """ Recursive """

    if low < high:
        mid = (low + high)//2 
        mergesort(A, low, mid)
        mergesort(A, mid+1, high)
        merge(A, low, mid, high)



A = [98, 00, 999, 99, 4,56,494,33,55,3,53,65,89,23,77,43,56]

print (A)

mergesort(A, 0, len(A)-1)

print (A)






