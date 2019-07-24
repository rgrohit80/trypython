arr = [2, 3, 4, 10, 40]


def binarySearch(arr, num, li, ri):
    if ri >= li:
        mid = li + (ri - li) // 2
        if num == arr[mid]:
            print(mid)
        elif num > arr[mid]:
            return binarySearch(arr, num, mid + 1, ri)
        elif num < arr[mid]:
            return binarySearch(arr, num, li, mid - 1)
    else:
        print('Not present')


binarySearch(arr, 10, 0, len(arr) - 1)
