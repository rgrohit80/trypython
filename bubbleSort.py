arr = [4, 3, 2, 1]

# ind = [0, 1, 2, 3]

def bubbleSort(arr):
    n = len(arr)
    for z in range(n, 1, -1):
        for i in range(z-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)


bubbleSort(arr)
