def insertionSort(arr): # traditional insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while (j>=0 and arr[j]) > key:
            arr[j+1]=arr[j]
            j=j-1
        
        arr[j+1] = key

def binaryInsertionSort(arr, item, start, end): # binary insertion sort
    if start == end:
        if arr[start] > item:
            return start
        else:
            return start+1
        



