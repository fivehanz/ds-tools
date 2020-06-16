
def partition(arr, low, high):
    """ using Lomuto's algorithm """
    pivot = A[high]
    i, j = low, low
    
    while j < high:
        if A[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
        j += 1

    temp = arr[i]
    arr[i] = arr[high]
    arr[high] = temp
    return i


def qsort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        qsort(arr, low, p-1)
        qsort(arr, p+1, high)



A = [98, 00, 999, 99, 4,56,494,33,55,3,53,65,89,23,77,43,56]

print (A)

qsort(A, 0, len(A)-1)
print (A)

A.append(12)
qsort(A, 0, len(A)-1)
print(A)