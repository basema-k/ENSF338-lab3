# Exercise 6 - Worst Case

import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)

def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

def quicksort_worst(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quicksort_worst(left) + [pivot] + quicksort_worst(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

# experiment

sizes = [10,20,50,100,200,500,1000,2000,5000,10000]

linear_times = []
qs_binary_times = []

for size in sizes:
    
    total_linear = 0
    total_qs_binary = 0
    
    for _ in range(100):
        
        arr = list(range(size)) 
        target = -1
        
        # Linear
        start = time.time()
        linear_search(arr, target)
        total_linear += time.time() - start
        
        # Worst-case quicksort & binary
        start = time.time()
        sorted_arr = quicksort_worst(arr.copy())
        binary_search(sorted_arr, target)
        total_qs_binary += time.time() - start
    
    linear_times.append(total_linear)
    qs_binary_times.append(total_qs_binary)

# plot

plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, qs_binary_times, label='Worst-Case Quick Sort + Binary')

plt.xlabel('Input Size (n)')
plt.ylabel('Total Time (100 runs)')
plt.title('Exercise 6 - Worst Case')
plt.legend()
plt.grid(True)
plt.savefig('ex6_worst_plot.png')
plt.show()

# In the worst-case scenario, linear search is faster than quick sort + binary search.
