import heapq


def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    min_heap = []

    for number in numbers:
        heapq.heappush(min_heap, number)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


print("Activity 4: Kth Largest")

numbers = [3, 2, 1, 5, 6, 4]

print("2nd largest:", kth_largest(numbers, 2))
print("4th largest:", kth_largest(numbers, 4))

# Verify using sorting
sorted_numbers = sorted(numbers, reverse=True)

print("Sorted list:", sorted_numbers)
print("2nd largest from sorting:", sorted_numbers[1])
print("4th largest from sorting:", sorted_numbers[3])