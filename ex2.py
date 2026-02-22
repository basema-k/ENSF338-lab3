# Exercise 2

import random
import time
import matplotlib.pyplot as plt

# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# quick sort
def quick_sort(arr):
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
    return quick_sort(left) + [pivot] + quick_sort(right)

# test sizes
sizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 
         60, 70, 80, 90, 100, 150, 200, 300, 400, 500]

bubble_best = []      # sorted
bubble_worst = []     # reverse sorted
bubble_avg = []       # random

quick_best = []       # random
quick_worst = []      # sorted
quick_avg = []        # random

for size in sizes:

    # bubble sort best
    arr = list(range(size))
    start = time.time()
    bubble_sort(arr.copy())
    bubble_best.append(time.time() - start)
    
    # bubble sort worst
    arr = list(range(size, 0, -1))
    start = time.time()
    bubble_sort(arr.copy())
    bubble_worst.append(time.time() - start)
    
    # bubble sort avg
    arr = [random.randint(1, 1000) for _ in range(size)]
    start = time.time()
    bubble_sort(arr.copy())
    bubble_avg.append(time.time() - start)
    
    # quick sort best
    arr = [random.randint(1, 1000) for _ in range(size)]
    start = time.time()
    quick_sort(arr.copy())
    quick_best.append(time.time() - start)
    
    # quick sort worst
    arr = list(range(size))
    start = time.time()
    quick_sort(arr.copy())
    quick_worst.append(time.time() - start)
    
    # quick sort avg
    arr = [random.randint(1, 1000) for _ in range(size)]
    start = time.time()
    quick_sort(arr.copy())
    quick_avg.append(time.time() - start)

plt.figure(figsize=(15, 4))

# best cases plot
plt.subplot(1, 3, 1)
plt.plot(sizes, bubble_best, 'b-o', label='Bubble Sort (sorted)')
plt.plot(sizes, quick_best, 'r-o', label='Quick Sort (random)')
plt.xlabel('Array Size')
plt.ylabel('Time (sec)')
plt.title('Best Cases')
plt.legend()
plt.grid(True)

# worst cases plot
plt.subplot(1, 3, 2)
plt.plot(sizes, bubble_worst, 'b-o', label='Bubble Sort (reverse sorted)')
plt.plot(sizes, quick_worst, 'r-o', label='Quick Sort (sorted)')
plt.xlabel('Array Size')
plt.ylabel('Time (sec)')
plt.title('Worst Cases')
plt.legend()
plt.grid(True)

# avg cases plot
plt.subplot(1, 3, 3)
plt.plot(sizes, bubble_avg, 'b-o', label='Bubble Sort (random)')
plt.plot(sizes, quick_avg, 'r-o', label='Quick Sort (random)')
plt.xlabel('Array Size')
plt.ylabel('Time (sec)')
plt.title('Average Cases')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('ex2_plots.png')
plt.show()