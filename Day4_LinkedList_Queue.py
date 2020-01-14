class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size=0


    def pushBack(self,key):
        node = Node(key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else :
            currenttail = self.tail
            currenttail.next = node
            self.tail = node
        self.size += 1

    def top_front(self):
        return self.head.value

    def pop_front(self):
        self.size -= 1
        head = self.head
        if head is None :
            raise Exception("Trying to pop from empty list")
        if self.head ==  self.tail:
            self.head = None
            self.tail = None
            return head.value
        self.head = head.next
        return head.value


    def print_linkedList(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode= currentnode.next

    def length(self):
        return self.size

    def isEmpty(self):
        return  self.size  == 0




class LinkedList_Queue:

    def __init__(self):
        self.queue = SinglyLinkedList()

    def enqueue(self,key):
        self.queue.pushBack(key)

    def dequeue(self):
        top = self.queue.top_front()
        self.queue.pop_front()
        return top

    def size(self):
        return self.queue.length()

    def empty(self):
        return  self.queue.isEmpty()

    def printQueue(self):
        return self.queue.print_linkedList()

_queue= LinkedList_Queue()

_queue.enqueue(10)
_queue.enqueue(20)
_queue.enqueue(30)
_queue.enqueue(40)

_queue.printQueue()

_queue.dequeue()
_queue.dequeue()
print("(((")
_queue.printQueue()