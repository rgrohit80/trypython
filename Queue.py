class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity-1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print('Full')
            return
        self.rear =


# # Implement Queue using stack
# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def enQueue(self, x):
#         self.s2 = self.s1[::-1]
#         self.s2.append(x)
#         self.s1 = self.s2[::-1]
#
#     # def enQueue(self, x):
#     #     while len(self.s1) != 0:
#     #         self.s2.append(self.s1[-1])
#     #         self.s1.pop()
#     #     self.s1.append(x)
#     #     while len(self.s2) != 0:
#     #         self.s1.append(self.s2[-1])
#     #         self.s2.pop()
#
#     def deQueue(self):
#         if len(self.s1) == 0:
#             print('the Q is Empty')
#         x = self.s1.pop()
#         return x
#
#     def qPrint(self):
#         print(self.s1)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     q.enQueue(1)
#     q.qPrint()
#     q.enQueue(2)
#     q.qPrint()
#     q.enQueue(3)
#     q.qPrint()
#     print(q.deQueue())
#     q.qPrint()
#     print(q.deQueue())
#     q.qPrint()
#     print(q.deQueue())
