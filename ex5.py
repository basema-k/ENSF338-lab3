def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def binarySearch(arr, item, start, end):
    if start == end:
        if arr[start] > item:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] < item:
        return binarySearch(arr, item, mid + 1, end)
    elif arr[mid] > item:
        return binarySearch(arr, item, start, mid - 1)
    else:
        return mid


def binaryInsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binarySearch(arr, key, 0, i - 1)

        # shift elements
        j = i - 1
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1

        arr[pos] = key
        
#2:

import random
import time
import matplotlib.pyplot as plt
import numpy as np

sizes = [100, 200, 400, 800, 1200, 1600]
tr_times = []
bin_times = []

for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]
    
    arr1 = arr.copy()
    start = time.perf_counter()
    insertionSort(arr1)
    tr_times.append(time.perf_counter() - start)

    arr2 = arr.copy()
    start = time.perf_counter()
    binaryInsertionSort(arr2)
    bin_times.append(time.perf_counter() - start)

#3:

plt.plot(sizes, tr_times, 'o-', label="Insertion Sort")
plt.plot(sizes, bin_times, 'o-', label="Binary Insertion Sort")

# Fit quadratic curves (since both are O(n^2))
z1 = np.polyfit(sizes, tr_times, 2)
z2 = np.polyfit(sizes, bin_times, 2)

p1 = np.poly1d(z1)
p2 = np.poly1d(z2)

x = np.linspace(min(sizes), max(sizes), 100)

plt.plot(x, p1(x), '--')
plt.plot(x, p2(x), '--')

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.title("Insertion Sort vs Binary Insertion Sort")
plt.show()

#4:
# Binary insertion sort is faster than traditional insertion sort. This is because it essentially eliminates half the possibilities at each step.

