# Exercise 7

import json
import time
import matplotlib.pyplot as plt

with open("ex7data.json", "r") as f:
    arr = json.load(f)

with open("ex7tasks.json", "r") as f:
    tasks = json.load(f)

def binary_search_custom(arr, target, first_mid_index):
    low = 0
    high = len(arr) - 1

    mid = first_mid_index

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

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

best_midpoints = []

n = len(arr)

candidates = list(range(0, n, max(1, n // 20)))  # ~20 evenly spaced choices

for target in tasks:

    best_time = float("inf")
    best_mid = None

    for mid_index in candidates:

        start = time.perf_counter()
        binary_search_custom(arr, target, mid_index)
        elapsed = time.perf_counter() - start

        if elapsed < best_time:
            best_time = elapsed
            best_mid = mid_index

    best_midpoints.append(best_mid)

# plot

plt.scatter(tasks, best_midpoints)

plt.xlabel("Search Task (Target Value)")
plt.ylabel("Best Initial Midpoint Index")
plt.title("Best First Midpoint per Search Task")

plt.show()

# 4:
# The choice of the initial midpoint does affect performance,
# If the initial midpoint happens to be closer to the target’s
# actual position in the array, the search finishes faster.
# However, because binary search halves the search space
# at every iteration, even a poor initial choice is quickly corrected.
