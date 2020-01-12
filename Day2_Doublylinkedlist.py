"""
Singly LinkedList implementation using Tail Pointer for better time complexity

for pushback and popback in O(1) times rather then O(N) times

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size=0

    def print_linkedList(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode= currentnode.next

    def push_front(self,key):
        node = Node(key)
        if self.head is None:
            self.head = node
            self.tail = node
        else :
            head = self.head
            self.head = node
            head.prev = node
            node.next = head
        self.size += 1

    def push_back(self,key):
        node = Node(key)
        if self.head is None :
            self.head = node
            self.tail = node
        else :
            current_tail = self.tail
            self.tail = node
            current_tail.next = node
            node.prev = current_tail

        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise Exception ("Trying to pop from empty list")
        if self.head == self.tail:
            head = self.head
            self.head = None
            self.tail = None
            return head
        else:
            currenthead = self.head
            head = currenthead.next
            self.head = head
            # set prev of head  to None you will foreget this remember it
            self.head.prev = None
            return  currenthead
        self.size -= 1

    def pop_back(self):
        if self.head is None:
            raise Exception ("Trying to pop from empty list")
        if self.head ==  self.tail :
            tail = self.tail
            self.head = None
            self.tail = None
            return  tail

        else :
            current_tail = self.tail
            self.tail = current_tail.prev
            self.tail.next = None

            return  current_tail
        self.size -= 1

    def addAfter(self,node,key):
        if node is  None:
            return
        # creating node
        new_node = Node(key)
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        if self.tail == node:
            self.tail =  new_node

    def find(self,key):
        head = self.head
        while head:
            if head.value == key:
                return head
            head = head.next
        return None

    def delete(self, key):
        _node =  self.find(key)
        # if we can't find the node to be deleted
        if _node  is None:
            return
        else:
            #  if deleteing head
            if self.head == _node:
                self.pop_front()
                return
            # if deleting tail
            elif self.tail == _node:
                self.pop_back()
                return
            # deleting middle node
            else:
                _previous = _node.prev
                _next = _node.next
                _previous.next = _next
                _next.prev = _previous
                return
    def addBefore(self,node,key):
        # 10 40  20 30
        # if node is not present
        if node is  None:
            return
        new_node = Node(key)
        new_node.next = node
        new_node.prev = node.prev
        node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        if self.head == node:
            self.head = new_node


    def length(self):
        return self.size

    def isEmpty(self):
        return  self.size  == 0




dl = DoublyLinkedList()
dl.push_front(10)

dl.push_back(20)
dl.push_back(30)

# dl.delete(30)

dl.addBefore(dl.find(30),40)
# dl.addAfter(dl.find(20),400)
# print("head {}  tail {} size {} ".format(dl.head.value,dl.tail.value,dl.size))

dl.print_linkedList()