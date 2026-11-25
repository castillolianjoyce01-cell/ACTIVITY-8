import heapq


def merge_arrays(arrays):
    min_heap = []

    for i in range(len(arrays)):
        if len(arrays[i]) > 0:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))

    result = []

    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)

        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heapq.heappush(
                min_heap,
                (next_value, array_index, next_index)
            )

    return result


print("Activity 5: Merge 3 Sorted Arrays")

array1 = [1, 4, 7, 10]
array2 = [2, 5, 8]
array3 = [3, 6, 9, 11, 12]

merged = merge_arrays([array1, array2, array3])

print("Merged array:", merged)