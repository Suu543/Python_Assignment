def selectionSort(L):
    n = len(L)
    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if (L[j] < L[minimum]):
                minimum = j
        
        temp = L[i]
        L[i] = L[minimum]
        L[minimum] = temp
    
    return L

def mergeSort(L):
    if (len(L) < 2):
        return L
        
    result = []
    mid = int(len(L) / 2)
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    
    result += left[left_index:]
    result += right[right_index:]

    return result    