import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def extract(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)


print("Activity 1: Min-Heap")

min_heap = MinHeap()

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for number in numbers:
    min_heap.insert(number)

print("Size:", min_heap.size())
print("Peek:", min_heap.peek())

print("Extracted values:")
while min_heap.size() > 0:
    print(min_heap.extract(), end=" ")

print()