#!/usr/bin/python3
class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private).
        __next_node (Node): The next node in the linked list (private).

    Methods:
        __init__(self, data, next_node=None): Initializes a new Node object with the given data and next_node.

    Properties:
        data (getter, setter): A property to get and set the data attribute.
        next_node (getter, setter): A property to get and set the next_node attribute.

    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data of the node.

        Returns:
            int: The data stored in the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next_node of the node.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node of the node.

        Args:
            value (Node): The new next_node in the linked list.

        Raises:
            TypeError: If value is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        __head (Node): The head node of the linked list (private).

    Methods:
        __init__(self): Initializes a new SinglyLinkedList object.
        sorted_insert(self, value): Inserts a new Node into the correct sorted position in the linked list.
        __str__(self): Converts the linked list to a string for printing.

    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList object.

        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list (increasing order).

        Args:
            value (int): The data to be stored in the new Node.

        """
        new_node = Node(value)

        # If the list is empty or the new value is smaller than the head's data, update the head
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            # Find the correct position to insert the new node
            while current.next_node is not None and current.next_node.data <= value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string for printing.

        Returns:
            str: The string representation of the linked list.

        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

