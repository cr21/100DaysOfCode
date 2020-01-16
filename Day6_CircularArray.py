class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.front = -1
        self.rear = -1
        self.arr = [0 for i in range(k)]
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.

        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % (len(self.arr))
        self.size += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1)%(len(self.arr))
            self.size -=1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return  self.arr[self.front]
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return  -1
        else:
            return self.arr[self.rear-1]
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.arr)

    # Your MyCircularQueue object will be instantiated and called as such:

#
# circularQueue = MyCircularQueue(3);
#
# # print("1 front {} Rear {} ".format(circularQueue.front,circularQueue.rear))
# print(circularQueue.enQueue(1))
#
# # print("2 front {} Rear {} ".format(circularQueue.front,circularQueue.rear))
# print(circularQueue.enQueue(2))
#
# # print("3 front {} Rear {} ".format(circularQueue.front,circularQueue.rear))
# print(circularQueue.enQueue(3))
# # print("4 front {} Rear {} ".format(circularQueue.front,circularQueue.rear))
# print(circularQueue.enQueue(4))
#
# print(circularQueue.arr)
#
# print(circularQueue.Rear());
# print(circularQueue.isFull());
# print(circularQueue.deQueue());
# print(circularQueue.enQueue(4));
# # print(circularQueue.arr)
# print(circularQueue.Rear());

queue =MyCircularQueue(6)
print(queue.enQueue(6)) # True
print("RearValue",queue.Rear()) # 6
print("Rear value",queue.Rear()) # 6
print(queue.deQueue()) #True
# print("Front after deque",queue.Front())
print(queue.enQueue(5))
print(queue.Rear())
print("Front before second deque",queue.front)
print(queue.deQueue())
print("Front",queue.Front())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())


"""

"""