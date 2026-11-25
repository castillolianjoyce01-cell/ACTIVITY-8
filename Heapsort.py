import heapq


def heap_sort(arr):
    heap = []

    for number in arr:
        heapq.heappush(heap, -number)

    sorted_arr = []

    while heap:
        sorted_arr.append(-heapq.heappop(heap))

    return sorted_arr


print("Activity 3: Heap Sort")

print(heap_sort([4, 10, 3, 5, 1]))
print(heap_sort([1, 2, 3, 4, 5]))       # Sorted array
print(heap_sort([5, 4, 3, 2, 1]))       # Reverse sorted
print(heap_sort([4, 2, 4, 1, 2]))        # Duplicates
print(heap_sort([]))                      # Empty array
print(heap_sort([7]))                     # Single element