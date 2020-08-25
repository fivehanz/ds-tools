"""
Mergesort
Inspired from Geeks4Geeks
Recursive
"""

def mergesort(A):
    if len(A) > 1:
        mid = len(A)//2
        Left, Right = A[:mid], A[mid:]
        
        mergesort(Left)
        mergesort(Right)
        
        i = j = k = 0
       
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                A[k] = Left[i]
                i+=1
            else:
                A[k] = Right[j]
                j+=1
            k+=1

        while i < len(Left):
            A[k] = Left[i]
            k+=1; i+=1
        
        while j < len(Right):
            A[k] = Right[j]
            k+=1; j+=1

     


A = [98, 00, 999, 99, 4,56,494,33,55,3,53,65,89,23,77,43,56]

print (A)

mergesort(A)
print (A)

A.append(12)
mergesort(A)
print(A)