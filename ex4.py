# Exercise 4

import sys
import time
import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(20000)

def quicksort_worst(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # first element pivot
    left = []
    right = []
    
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quicksort_worst(left) + [pivot] + quicksort_worst(right)

# test sizes
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
times = []

print("Size | Time (sec)")
print("-" * 20)

for size in sizes:
    # sorted array of given size
    arr = list(range(size))
    
    start = time.time()
    quicksort_worst(arr)
    elapsed = time.time() - start
    times.append(elapsed)
    
    print(f"{size:4d} | {elapsed:.4f}")

plt.plot(sizes, times, 'bo-')
coeffs = np.polyfit(sizes, times, 2)
quadratic_fit = np.polyval(coeffs, sizes)
plt.plot(sizes, quadratic_fit, 'r--')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (sec)')
plt.title("Quick Sort Worst Case (Sorted Input)")
plt.grid(True)
plt.savefig('ex4_plot.png')
plt.show()