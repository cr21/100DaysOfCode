class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size=0

    def pushFront(self,key):
        node = Node(key)
        if self.head is not None:
            currenthead = self.head
            node.next = currenthead
            self.head=node
        else:
            self.head = node
        self.size+=1

    def pushBack(self,key):
        node = Node(key)
        currentnode = self.head

        if currentnode is None:
            self.head = node
            self.size +=1
            return
        while currentnode.next:
            currentnode = currentnode.next
        currentnode.next = node
        self.size += 1

    def popBack(self):
        currentnode = self.head
        if currentnode.next is None:
            self.head = None
            return currentnode
        while currentnode.next.next:
            currentnode = currentnode.next
        popped = currentnode.next
        currentnode.next = None
        self.size -= 1
        return popped

    def top_front(self):
        return self.head.value

    def pop_front(self):
        self.size += 1
        if self.head is not None:
            currenthead = self.head
            self.head = self.head.next
            return currenthead
        return None

    def print_linkedList(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode= currentnode.next

    def length(self):
        return self.size

    def isEmpty(self):
        return  self.size  == 0


    def addAfter(self,_Node,key):
        node = Node(key)
        currentnode = self.head
        while currentnode:
            if currentnode.value == _Node:
                nextnode = currentnode.next
                currentnode.next = node
                node.next = nextnode
                return
            currentnode = currentnode.next


    def find(self,key):
        currentnode = self.head
        while currentnode:
            if currentnode.value == key:
                return True
            currentnode =  currentnode.next
        return False




    def addBefore(self,_Node,key):

        node = Node(key)
        currentnode = self.head
        if currentnode and _Node == currentnode.value:
            self.head = node
            node.next = currentnode
            return

        if currentnode.next is None:
            node.next = currentnode
            return

        while currentnode.next:
            # print("***")
            if currentnode.next.value == _Node:
                node.next = currentnode.next
                currentnode.next = node
                return
            currentnode =  currentnode.next

    def delete(self,key):
        currentnode = self.head
        if currentnode and currentnode.value == key:
            self.head = currentnode.next
            return
        while currentnode.next:
            if currentnode.next.value == key:
                foundednode =currentnode.next
                currentnode.next = foundednode.next
                return
            currentnode =  currentnode.next

ll = LinkedList()

ll.pushFront(10)
ll.pushFront(20)
ll.pushFront(30)

ll.pushBack(40)
ll.pushBack(50)
ll.pushBack(60)

ll.print_linkedList()
