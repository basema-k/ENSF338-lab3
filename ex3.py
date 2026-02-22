# Exercise 3

import random
import matplotlib.pyplot as plt

def bubble_sort_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return comparisons, swaps

# test sizes
sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
comps_list = []
swaps_list = []

print("Size | Comparisons | Swaps")
print("-" * 30)

for size in sizes:
    # random array of given size
    arr = [random.randint(1, 100) for _ in range(size)]
    comps, swaps = bubble_sort_count(arr)
    comps_list.append(comps)
    swaps_list.append(swaps)
    print(f"{size:4d} | {comps:10d} | {swaps:5d}")


plt.figure(figsize=(12, 4))

# comparisons plot
plt.subplot(1, 2, 1)
plt.plot(sizes, comps_list, 'bo-')
plt.plot(sizes, [n*(n-1)/2 for n in sizes], 'r--')
plt.xlabel('Size (n)')
plt.ylabel('Comparisons')
plt.title('Actual vs n(n-1)/2')
plt.legend(['Actual', 'Formula'])
plt.grid(True)

# swaps plot
plt.subplot(1, 2, 2)
plt.plot(sizes, swaps_list, 'go-')
plt.plot(sizes, [n*(n-1)/4 for n in sizes], 'r--')
plt.xlabel('Size (n)')
plt.ylabel('Swaps')
plt.title('Actual vs n(n-1)/4')
plt.legend(['Actual', 'Formula'])
plt.grid(True)

plt.tight_layout()
plt.savefig('ex3_plots.png')
plt.show()