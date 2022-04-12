""" 
Countsort 
time: n+n => O(n)
space: O(n)
"""


def findMax(arr):
    max = 0
    for e in arr:
        if e > max:
            max = e
    return max


def countSort(A):
    N = len(A)
    max = findMax(A)
    countA = [0] * (max + 1)

    i = 0
    while i < N:
        countA[A[i]] += 1
        i += 1

    i = j = 0
    while i <= max:
        for k in range(countA[i]):
            A[j] = i
            j += 1
            countA[i] - + 1
        i += 1


A = [99, 00, 99, 99, 4, 56, 49, 33, 55, 3, 53, 65, 89, 23, 77, 43, 56]

print(A)

countSort(A)
print(A)

A.append(12)
countSort(A)
print(A)
