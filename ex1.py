# Exercise 1 - NOT COMPLETE

from heapq import merge
import sys
sys.setrecursionlimit(20000)

arr = [8, 42, 25, 3, 3, 2, 27, 3]
original_arr = arr.copy()

def merge(arr, low, mid, high):

    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0    # pointers for sides
    k = low    # pointer for replacing original array

    while i < len(left) and j < len(right):
        # if left half has next smallest element
        if left[i] <= right[j]:
            arr[k] = left[i]    # put next in original array
            i += 1
        else:    # if right side has next smallest element
            arr[k] = right[j]
            j += 1    # move to next element if already added
        k += 1

    while i < len(left):    # if only left half is left
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):    # if only right half is left
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

merge_sort(arr, 0, len(arr) - 1)

print("Original array:", original_arr)
print("Sorted array:", arr)