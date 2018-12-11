class MinHeap():
    '''
    valid indexes are between i <= size and i >= 1
    left child = 2i
    right child = 2i+1
    parent = i/2
    '''
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def validIndex(self, index):
        return index <= self.size and index > 0

    def heapPropertyViolated(self, parent, child):
        if self.validIndex(parent) and self.validIndex(child):
            return self.heap[parent] > self.heap[child]
        else:
            return False

    def min(self):
        if self.size > 0:
            return self.heap[1]
        else:
            raise ValueError

    def heapifyUp(self, index):
        while self.validIndex(index//2) and self.heap[index] < self.heap[index//2]:
                self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
                index = index//2

    def heapifyDown(self, index):
        if self.validIndex(index) and (self.heapPropertyViolated(index, 2*index) or self.heapPropertyViolated(index, 2*index+1)):
            if self.heapPropertyViolated(index, 2*index) and (self.validIndex(2*index+1) and self.heap[2*index] < self.heap[2*index+1]):
                self.heap[index],self.heap[2*index] = self.heap[2*index],self.heap[index]
                self.heapifyDown(2*index)
            elif self.heapPropertyViolated(index, 2*index+1) and (self.validIndex(2*index) and self.heap[2*index+1] < self.heap[2*index]):
                self.heap[index],self.heap[2*index+1] = self.heap[2*index+1],self.heap[index]
                self.heapifyDown(2*index+1)


    def insert(self, value):
        # the empty slot is at heap[size]
        self.heap.append(value)
        self.heapifyUp(self.size+1)
        self.size += 1

    def deleteMin(self):
        min = self.min()
        last_element = self.heap[self.size]
        self.heap[1] = last_element
        self.heapifyDown(1)
        del self.heap[self.size]
        self.size-=1
        return min

h = MinHeap()
h.insert(9)
print(h.heap)
h.insert(8)
print(h.heap)
h.insert(13)
print(h.heap)
h.insert(5)
print(h.heap)
h.insert(4)
print(h.heap)
h.deleteMin()
print(h.heap)
h.deleteMin()
print(h.heap)
h.deleteMin()
print(h.heap)
h.deleteMin()
print(h.heap)
h.deleteMin()
print(h.heap)
