'''Binary Heap implementation using a priority queue.'''

class BinaryHeap():

    def __init__(self, elems=None):
        heap = list()

    def add(self, elem):
        self.heap.append(elem)
        self.swim(len(self.heap) -1)

    def swim(self, elem_index):
        parent = int((elem_index -1)/2)
        while(elem_index > 0 and self.heap[elem_index] < self.heap[parent]):
            swap(elem_index, parent)
            elem_index = parent
            parent = int((elem_index-1)/2)

    def sink(self, elem_index):
        while(elem_index >= len(self.heap)):
            left = 2*elem_index + 1
            right = 2*elem_index + 2
            if (left > len(self.heap)) and (right > len(self.heap)):
                break
            smallest = left
            if (right < len(self.heap)-1) and (self.heap[left] >= self.heap[right]):
                smallest = right
            swap(elem_index, smallest)
            elem_index = smallest

    def poll(self):
        self.removeAt(0)

    def remove(self, elem):
        elem_index = self.contains(elem)
        if elem_index == -1:
            raise NotFoundException("Element {} not in heap.".format(elem))
        self.removeAt(elem_index)


    def contains(self, elem):
        elem_index = -1
        for i in range(len(self.heap)):
            if self.heap[i] == elem:
                elem_index = i
                break
        return elem_index

    def swap(self, elem1_index, elem2_index):
        temp = self.heap[elem1_index]
        self.heap[elem1_index] = self.heap[elem2_index]
        self.heap[elem1_index] = temp

    def peek(self):
        if !isEmpty():
            return self.heap[0]

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.heap)

    def clear(self):
        self.heap = list()



