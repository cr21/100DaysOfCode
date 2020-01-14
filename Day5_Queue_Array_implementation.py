class Queue :
    def __init__(self):
        self.arr = [0 for i in range(5)]
        self.frontIndex = -1
        self.size = 0

    def enqueue(self,key):
        if self.empty():
            self.frontIndex = 0
        if self.full():
            self.arr = self.increaseQueueCapacity(self.arr)
        self.arr[self.frontIndex] = key
        self.frontIndex += 1
        self.size += 1


    def full(self):
        return self.size == len(self.arr)


    def dequeue(self):
        if self.empty():
            raise Exception("Trying to dequeue from empty queue")
        else:
            popped_element = self.arr[0]
            for i in range(len(self.arr)-1):
                self.arr[i] = self.arr[i+1]
            self.size -= 1
            self.frontIndex -= 1
            return popped_element

    def empty(self):
        return  self.size == 0

    def length(self):
        return q.size

    def printQueue(self):
        for item in  self.arr:
            print(item)
        return

    def increaseQueueCapacity(self,arr):
        self.arr = [-1 for i in range(len(arr) * 2)]
        # copying temp_arr into new array
        for i in range(len(arr)):
            self.arr[i] = arr[i]
        return self.arr
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Front index",q.frontIndex)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("Front index",q.frontIndex)
q.printQueue()

