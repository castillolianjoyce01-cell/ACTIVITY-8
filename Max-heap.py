import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return -self.heap[0]

    def extract(self):
        if len(self.heap) == 0:
            return None
        return -heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)


print("Activity 2: Max-Heap")

max_heap = MaxHeap()

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for number in numbers:
    max_heap.insert(number)

print("Size:", max_heap.size())
print("Peek:", max_heap.peek())

print("Extracted values:")
while max_heap.size() > 0:
    print(max_heap.extract(), end=" ")

print()