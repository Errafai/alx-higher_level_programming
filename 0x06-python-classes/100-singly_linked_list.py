#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, object):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:


    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None or value < self.head.data:
            new.next_node = self.head
            self.head = new
        else:
            curr = self. head
            while curr.next_node is not None \
                  and curr.next_node.data < new.data:
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new

    def __str__(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(result)
