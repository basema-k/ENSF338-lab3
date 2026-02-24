# Exercise 6 - Average Case

import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)

def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

def quick_sort(arr):
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
    
    return quick_sort(left) + [pivot] + quick_sort(right)

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
        random.shuffle(arr)
        target = -1  # not in array
        
        # Linear search timing
        start = time.time()
        linear_search(arr, target)
        total_linear += time.time() - start
        
        # Quick sort + binary search timing
        start = time.time()
        sorted_arr = quick_sort(arr.copy())
        binary_search(sorted_arr, target)
        total_qs_binary += time.time() - start
    
    linear_times.append(total_linear)
    qs_binary_times.append(total_qs_binary)

# plot

plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, qs_binary_times, label='Quick Sort + Binary Search')

plt.xlabel('Input Size (n)')
plt.ylabel('Total Time (100 runs)')
plt.title('Exercise 6 - Average Case')
plt.legend()
plt.grid(True)
plt.savefig('ex6_avg_plot.png')
plt.show()

# For average-case inputs, linear search is faster.
# Linear search runs in O(n).
# Quick sort + binary search runs in O(n log n)
