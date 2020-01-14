class List_Queue:
    def __init__(self):
        self.queue = list()
        self.size = 0

    def enqueue(self,key):
        self.queue.append(key)
        self.size += 1
    def dequeue(self):
        if self.empty():
            raise  Exception("Can't pop item from empty list")
        else:
            self.size -= 1
            return  self.queue.pop(0)

    def empty(self):
        return self.size == 0

    def printQueue(self):
        for item in self.queue:
            print(item)
queue = List_Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.printQueue()

print(queue.dequeue())
print(queue.dequeue())
