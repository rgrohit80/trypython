class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev, data):
        new_node = Node(data)
        if prev is None:
            print('the prev node must be in Linked List')
            return
        new_node.next = prev.next
        prev.next = new_node

    def append(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def palindrome(self):
        temp = self.head
        lista = []
        while temp:
            lista.append(temp.data)
            temp = temp.next
        if lista == lista[::-1]:
            print('Palindrome')
        else:
            print('Not palindrome')

    def reverse(self):
        temp = self.head
        len = 0
        while temp.next:
            len += 1
            temp = temp.next
        for i in range(len - 1):
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            temp.next = tmp
            temp = tmp

    def removedupli(self):
        temp = self.head
        while temp:
            if temp.data == temp.next.data:
                next = temp.next.next
                temp.next = None
                temp.next = next
                temp = temp.next
            else:
                temp = temp.next
        print('-------------')
        self.printList()

    def swapnodes(self, x, y):
        temp = self.head



    def removedunsort(self):
        temp = self.head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(1)
    llist.push(3)
    llist.push(3)
    llist.push(5)
    llist.push(6)
    llist.printList()
    llist.removedupli()
    print('-------------')
