'''
    Actual code is on https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/.
    This is a re-implementation to check my own understanding.
'''

import ctypes

class DynamicArray(object):

    def __init__(self, capacity=1):
        self.n = 0
        self.capacity = capacity
        self.A = self.make_array(self.capacity)
        for i in range(self.capacity):
            self.A[i] =0

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if self.isEmpty():
            print("Array Empty !!!")
        if self.verify_index(index):
            return self.A[index]
        return None

    def isEmpty(self):
        return self.n == 0

    def verify_index(self, index):
        ''' Flags incorrect index.'''
        ret = False
        if 0 <= index < self.n:
            ret = True
        return ret

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def _resize(self, scale_factor=2):

        if self.capacity == 0:
            new_capacity = 1
        else:
            new_capacity = self.capacity*scale_factor
        new_array = self.make_array(new_capacity)
        for i in range(len(self.A)):
            new_array[i] = self.A[i]
        self.A = new_array

    def append(self, value):

        if self.n == self.capacity:
            self._resize()
        self.A[self.n] = value
        self.n += 1

    def delete(self):
        ''' Delete an item from the end.'''

        if self.isEmpty():
            print("Array Empty, nothing to delete.")
            return None
        self.A[self.n-1] = 0
        self.n -= 1

    def removeAt(self, index):
        ''' Delete an item at an index.'''

        if self.isEmpty():
            print("Array Empty, nothing to delete.")
            return None
        if self.verify_index(index):
            for i in range(index, self.n):
                self.A[i] = self.A[i+1]
            self.n -= 1

    def insertAt(self, index, value):
        ''' Insert an item at an index.'''

        if self.verify_index(index):
            if self.n == self.capacity:
                self.resize()
            for i in range(self.n, index-1, -1):
                self.A[i] = self.A[i-1]
            self.A[index] = value
            self.n += 1

    def show(self):
        ''' Display array items.'''

        for i in range(self.n):
            print("{} ".format(self.A[i]))
