# Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class

class LinkedList:
    def __init__(self):
        self.head = None

    # This function is in LinkedList class
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('the given previous node be must be in linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, key):

        temp = self.head

        # if we need to delete the first Node

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.push(12)
    llist.insertAfter(second, 200)
    llist.append('append')
    llist.printList()
