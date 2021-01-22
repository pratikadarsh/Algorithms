'''
    Implementation of Single Linked List.
'''

class Node():

    def __init__(self, data, next):
        self.data = data
        self.next = next
        self.travIter = None

    def __repr__(self):
        return self.data

class SingleLinkedList():

    def __init__(self):
        self.llsize = 0
        self.head = None
        self.tail = None

    def __len__(self):
        """
        Return number of elements sorted in array.
        """
        return self.llsize

    def clear(self):
        """
        Empty this linked list, O(n)
        """
        tempNode = self.head
        while tempNode != None:
            next = tempNode.next
            tempNode.data = None
            tempNode.next = None
            tempNode = next
            self.llsize -= 1
        self.head = None
        self.tail = None

    def size(self):
        """
        Return the size of this linked list
        """
        return self.llsize


    def isEmpty(self):
        """
        Is this linked list empty?
        """
        return self.size() == 0

    def add(self, elem):
        """
        Add an element to the tail of the linked list, O(1)
        """
        self.addLast(elem)

    def addLast(self, elem):
        """
        Add a node to the tail of the linked list, O(1).
        """
        if self.isEmpty():
            self.head = self.tail = Node(elem, None)
        else:
            self.tail.next = node = Node(elem, None)
            self.tail = self.tail.next
        self.llsize += 1

    def addFirst(self, elem):
        """
        Add an element to the beginning of this linked list, O(1).
        """
        if self.isEmpty():
            self.head = self.tail = Node(elem, None)
        else:
            node = Node(elem, self.head)
            self.head = node
        self.llsize += 1

    def addAt(self, index, data):
        """
        Add an element at a specified index
        """
        if index < 0 or index > self.llsize:
            raise Exception("Index out of range.")
        if index == 0:
            self.addFirst(data)
            return
        if index == self.llsize:
            self.addLast(data)
            return

        currNode = self.head
        for i in range(index-1):
            currNode = currNode.next
        node = Node(data, currNode.next)
        currNode.next = node
        self.llsize += 1


    def peekFirst(self):
        """
        Check the value of the first node if it exists, O(1)
        """
        if self.isEmpty():
            print("Linked List Empty !!!")
        else:
            return self.head.data

    def peekLast(self):
        """
        Check the value of the last node if it exists, O(1)
        """
        if self.isEmpty():
            print("Linked List Empty !!!")
        else:
            return self.tail.data

    def removeFirst(self):
        """
        Remove the first value at the head of the linked list, O(1)
        """
        if self.isEmpty():
            print("Linked List Empty !!!")
            return None
        tempnode = self.head
        self.head = self.head.next
        self.llsize -= 1
        if self.isEmpty():
            self.tail = None
        data = tempnode.data
        tempnode.data = None
        tempnode.next = None
        return data

    def removeLast(self):
        """
        Remove the last value at the tail of the linked list, O(1)
        """
        if self.isEmpty():
            print("Linked List Empty !!!")
            return None
        tempnode = None
        if self.size() == 1:
            tempnode = self.head
            self.head = self.tail = None
        else:
            currnode = self.head
            while currnode.next != self.tail:
                currnode = currnode.next
            tempnode = currnode.next
            currnode.next = None
            self.tail = currnode
        self.llsize -= 1
        data = tempnode.data
        tempnode.data = tempnode.next = None
        return data

    def __remove__(self, node):
        """
        Remove an arbitrary node from the linked list, O(1)
        """
        if self.head == node:
            self.removeFirst()
        if self.tail == node:
            self.removeLast()
        tempnode = self.head
        while tempnode.next != node:
            tempnode = tempnode.next
            if tempnode == None:
                raise Exception("Node {} not present in the list.".format(node))
        removednode = tempnode.next
        tempnode.next = tempnode.next.next
        self.llsize -= 1
        data = removednode.data
        removednode.data = removednode.next = None
        return data

    def removeAt(self, index):
        """
        Remove a node at a particular index, O(n)
        """
        if index < 0 or index >= self.size():
            raise ValueError("Index out of range.")
        data = None
        if index == 0:
            data = self.removeFirst()
        if index == self.size() -1:
            data = self.removeLast()
        else:
            tempnode = self.head
            for i in range(index):
                tempnode = tempnode.next
            data = self.__remove__(tempnode)
        return data



    def remove(self, obj):
        """
        Remove a particular value in the linked list, O(n)
        """
        currnode = self.head
        data = None
        while currnode != None:
            if currnode.data == obj:
                data = self.__remove__(currnode)
                break
            else:
                currnode = currnode.next
        if data == None:
            raise Exception("Value: {} not found in the list.".format(obj))
        return data

    def indexOf(self, obj):
        """
        Find the index of a particular value in the linked list, O(n)
        """
        currnode = self.head
        pos = -1
        for i in range(self.size()):
            if currnode.data == obj:
                pos = i
                break
            else:
                currnode = currnode.next
        if pos == -1:
            raise Exception("Value: {} not found in the list.".format(obj))
        return pos

    def contains(self, obj):
        """
        Check if a value is contained within the linked list
        """
        return self.indexOf(obj) != -1

    def __iter__(self):
        """
        Called when iteration is initialized
        """
        self.travIter = self.head
        return self

    def __next__(self):
        """
        To move to next element.
        """
        # Stop iteration if limit is reached
        if self.travIter is None:
            raise StopIteration

        # Store current travIter.data
        data = self.travIter.data
        self.travIter = self.travIter.next

        # Else increment and return old value
        return data

    def __repr__(self):
        sb = ""
        sb = sb + '[ '
        trav = self.head
        while trav is not None:
            sb = sb + str(trav.data)
            if trav.next is not None:
                sb = sb + ', '
            trav = trav.next
        return str(sb) + "]"
