

def bubleSort(arr):
    n = len(arr)
    for ran in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubleSort([800, 11, 50, 771, 649, 770, 240, 9]))
